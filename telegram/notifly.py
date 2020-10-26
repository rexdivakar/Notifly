# -*- coding: UTF8 -*-
import requests
import sys
import json
from os import path

token = ''  # Token of your bot


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    # url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, msg):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']

        params = {'chat_id': chat_id, 'text': msg, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        return requests.post(self.api_url + method, params)

    def send_image(self, img_path):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']
        method = 'sendPhoto?'+'chat_id='+str(chat_id)

        files = {'photo': open(img_path, 'rb')}

        return requests.post(self.api_url+method, files=files)
    
    def __append_messages(self, messages, fetch_updates, message_path):
        if len(fetch_updates) == 0: return []

        with open('./message/conversation.json', 'w+') as json_file:
            for update in fetch_updates:
                message_exist = any(
                    message['update_id'] == update['update_id']
                    for message in messages
                )

                if message_exist is False:
                    messages.append(update)

            json.dump(
                messages,
                json_file,
                indent=4,
                separators=(", ", ": "),
                sort_keys=True
            )

    def receive_messages(self, message_path='./message/conversation.json'):
        try:
            fetch_updates = self.get_updates()

            messages = []
            
            if path.exists(message_path):
                read_file = open(message_path, 'r')
                messages = json.load(read_file)
                
                self.__append_messages(messages, fetch_updates, message_path)
                
                read_file.close()
            else:
                self.__append_messages(messages, fetch_updates, message_path)

            return messages
        except Exception:
            print('Unexpected error:', sys.exc_info())

            return []
