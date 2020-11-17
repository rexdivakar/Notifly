"""Discord API webhooks wrapper"""

import requests


class Notifier:
    def __init__(self, webhooks):
        """
        Initialize the Discord Webhook instance

        :argument webhooks: -> Discord webhook token [Mandatory]
        :return: the response of webhook status
        """

        self.__webhooks = webhooks
        self.payload = None
        try:
            if requests.get(self.__webhooks).status_code == 401:
                raise ConnectionError('Invalid Webhook')
        except Exception as err:
            print(err)
            exit(1)
        #TODO Handle Network Error

    def send_message(self, msg):
        """
        send_message -> function to post message to the discord channel

        :argument msg: -> Posts message to the discord channel [String] [UTF-8]
        :return: response to the message post
        """
        payload = {'content': str(msg)}
        try:
            return requests.post(url = self.__webhooks, data = payload)
        except ConnectionError as cer:
            print(cer)

    def send_file(self, file_path):
        """
        send_image -> function to post an image to the discord channel

        :argument file_path: -> enter the path of the file to be sent
        :return: response to the message post
        """
        try:
            self.payload = {'file': open(file_path, 'rb')}
        except FileNotFoundError as fl_er:
            print(fl_er)
            exit(1)
        try:
            return requests.post(url = self.__webhooks, files = self.payload)
        except OverflowError as err:
            print('Size Overflow Error', err)
