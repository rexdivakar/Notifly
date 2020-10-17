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

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp


magnito_bot = BotHandler(token)  # Your bot's name


fetch_updates = magnito_bot.get_updates()

chat_id = fetch_updates[0]['message']['chat']['id']
update_id = fetch_updates[0]['update_id']


def main():
    msg = sys.argv[1]   # fetch message

    if len(sys.argv) > 2:
        print('Invalid Argument')
    else:
        return magnito_bot.send_message(chat_id=chat_id, text=msg)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
