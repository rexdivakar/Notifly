# -*- coding: UTF8 -*-
import json
import os
import requests


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

        params = {'chat_id': chat_id, 'text': msg,
                  'parse_mode': 'HTML', 'disable_notification': notification}
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
            file_name = ''
            media = ['document', 'photo', 'video', 'voice']
            # Check if update message contains any of the media keys from above
            intersection = list(set(update['message'].keys()) & set(media))
            if intersection:
                media_key = intersection[0]

                # Determine file_id. For photos multiple versions exist. Use the last one.
                if media_key == 'photo':
                    file_id = update['message'][media_key][-1]['file_id']
                else:
                    file_id = update['message'][media_key]['file_id']

                if media_key == 'document':
                    # In a document, it's possible to use the original name.
                    file_name = update['message'][media_key]['file_name']
                self.get_file(file_id, file_name)

    def get_file(self, file_id, filename=''):
        """"Follow the getFile endpoint and download the file by file_id.
        A fileName can be given, else a file_unique_id gibberish name will be used.
        See also: https://core.telegram.org/bots/api#getfile
        """
        method = 'getFile?' + 'file_id=' + str(file_id)
        res = requests.post(self.api_url + method, file_id)
        try:
            file_path = res.json()['result']['file_path']
            # Determine the fileName. Use modified file_path if none given.
            if not filename:
                filename = file_path[file_path.rfind('/') + 1:]
        except (KeyError, ValueError):
            return "500 - Failed parsing the file link from API response."

        if not os.path.exists(self.dirDownloads):
            os.mkdir(self.dirDownloads)

        local_path = os.path.join(self.dirDownloads, filename)

        # Download file as stream.
        res = requests.get(self.file_url + file_path, stream=True)
        if res.status_code == 200:
            try:
                with open(local_path, 'wb') as f:
                    for chunk in res:
                        f.write(chunk)
            except IOError:
                pass
            return '200 - {} written.'.format(local_path)
        else:
            return '404 - Error accessing {}'.format(file_path)

    def session_dump(self):
        resp = self.get_updates()
        try:
            if not os.path.exists(self.dirDownloads):
                os.mkdir(self.dirDownloads)
            localPath = os.path.join(self.dirDownloads, 'session_dump.json')

            with open(localPath, 'w+', encoding='utf-8') as outfile:
                json.dump(resp, outfile)
        except:
            return 'Dump Error'
