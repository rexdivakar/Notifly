"""Discord API webhooks wrapper"""

import requests


class Notifier:
    def __init__(self, webhooks):
        """
        Initialize the Discord Webhook instance

        Args:
            webhooks (basestring): Discord webhook token [Mandatory]
        Returns:
            The response of webhook status
        Raises:
            ConnectionError, Exception
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

    def send_message(self, msg) -> object:
        """
        Function to post message to the discord channel

        Args:
            msg (string): Posts message to the discord channel [String] [UTF-8]
        Returns:
            The response to the message on post operation.
        Raises:
            ConnectionError
        """
        payload = {'content': str(msg)}
        try:
            return requests.post(url = self.__webhooks, data = payload)
        except ConnectionError as cer:
            print(cer)

    def send_file(self, file_path) -> object:
        """
        Function to post an image to the discord channel

        Args:
            file_path (string): Enter the path of the file to be sent
        Returns:
            The response to the message on post operation.
        Raises:
            FileNotFoundError, OverflowError
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
