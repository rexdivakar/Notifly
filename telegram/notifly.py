# -*- coding: UTF8 -*-
import requests
import datetime
import sys

token = ''  # Token of your bot


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, msg,notification):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']
        # update_id = fetch_updates[0]['update_id']
        
        params = {'chat_id': chat_id, 'text': msg, 'parse_mode': 'HTML','disable_notification':notification}
        method = 'sendMessage'
        return requests.post(self.api_url + method, params)

    def send_image(self,img_path,notification):
        fetch_updates = self.get_updates()
        chat_id = fetch_updates[0]['message']['chat']['id']
        
        files={'photo':open(img_path, 'rb')}
        
        method = 'sendPhoto?'+'chat_id='+str(chat_id)+str(notification)


        resp = requests.post(self.api_url+method,files=files)
