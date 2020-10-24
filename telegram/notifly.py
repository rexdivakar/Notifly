# -*- coding: UTF8 -*-
import json
import os

import requests

token = ''  # Token of your bot


class BotHandler:
    def __init__(self, token, dirdownloads='./downloads'):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.file_url = "https://api.telegram.org/file/bot{}/".format(token)
        self.dirDownloads = dirdownloads

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        try:
            return resp.json()['result']
        except:
            return '404 error'

    def send_message(self, msg, notification):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']
        # update_id = fetch_updates[0]['update_id']

        params = {'chat_id': chat_id, 'text': msg, 'parse_mode': 'HTML', 'disable_notification': notification}
        method = 'sendMessage'
        return requests.post(self.api_url + method, params)

    def send_image(self, img_path):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']
        method = 'sendPhoto?' + 'chat_id=' + str(chat_id)

        files = {'photo': open(img_path, 'rb')}
        return requests.post(self.api_url + method, files=files)

    def send_document(self, file_path):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']
        method = 'sendDocument?' + 'chat_id=' + str(chat_id)

        files = {'document': open(file_path, 'rb')}
        return requests.post(self.api_url + method, files=files)

    def download_files(self):
        fetch_updates = self.get_updates()
        for update in fetch_updates:
            fileName = ''
            media = ['document', 'photo', 'video', 'voice']
            # Check if update message contains any of the media keys from above
            intersection = list(set(update['message'].keys()) & set(media))
            if intersection:
                mediaKey = intersection[0]

                # Determine fileId. For photos multiple versions exist. Use the last one.
                if mediaKey == 'photo':
                    fileId = update['message'][mediaKey][-1]['file_id']
                else:
                    fileId = update['message'][mediaKey]['file_id']

                if mediaKey == 'document':
                    # In a document, it's possible to use the original name.
                    fileName = update['message'][mediaKey]['file_name']
                self.get_file(fileId, fileName)

    def get_file(self, file_id, filename=''):
        """"Follow the getFile endpoint and download the file by file_id.
        A fileName can be given, else a file_unique_id gibberish name will be used.

        See also: https://core.telegram.org/bots/api#getfile
        """
        method = 'getFile?' + 'file_id=' + str(file_id)
        res = requests.post(self.api_url + method, file_id)
        try:
            filePath = res.json()['result']['file_path']
            # Determine the fileName. Use modified filePath if none given.
            if not filename:
                filename = filePath[filePath.rfind('/') + 1:]
        except (KeyError, ValueError):
            return "500 - Failed parsing the file link from API response."

        if not os.path.exists(self.dirDownloads):
            os.mkdir(self.dirDownloads)

        localPath = os.path.join(self.dirDownloads, filename)

        # Download file as stream.
        res = requests.get(self.file_url + filePath, stream=True)
        if res.status_code == 200:
            try:
                with open(localPath, 'wb') as f:
                    for chunk in res:
                        f.write(chunk)
            except IOError:
                pass
            return '200 - {} written.'.format(localPath)
        else:
            return '404 - Error accessing {}'.format(filePath)

    def session_dump(self):
        '''
        Session Download manager
        '''
        resp = self.get_updates()
        try:
            if not os.path.exists(self.dirDownloads):
                os.mkdir(self.dirDownloads)
            localPath = os.path.join(self.dirDownloads, 'session_dump.json')

            with open(localPath, 'w+', encoding='utf-8') as outfile:
                json.dump(resp, outfile)
        except:
            return 'Dump Error'
