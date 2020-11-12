import requests


class Notifier:
    """Discord API webhooks wrapper"""
    def __init__(self, webhooks):
        self.__webhooks = webhooks

    def send_message(self, msg):
        payload = {'content': str(msg)}
        try:
            return requests.post(url = self.__webhooks, data=payload)
        except ConnectionError as cer:
            print(cer)

    def send_file(self, file_path):
        try:
            files = {'file': open(file_path, 'rb')}
        except FileNotFoundError as fl_er:
            print(fl_er)
            exit()
        try:
            return requests.post(url = self.__webhooks, files = files)
        except OverflowError as err:
            print('Size Overflow Error',err)
