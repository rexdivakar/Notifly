"""Discord API webhooks wrapper"""

import requests
from notifly.tf_notifier import TfNotifier
from requests import exceptions


class Notifier(TfNotifier):

    class __AuthError(Exception):
        """
        Authentication Exception
        """
        pass

    def __init__(self, webhooks):
        """
        Initialize the Discord Webhook instance

        Args:
            webhooks (basestring): Discord webhook token [Mandatory]
        Returns:
            The response of webhook status
        Raises:
            Exception, AuthError, MissingSchema
        """
        self.__webhooks = webhooks
        self.payload = None

        try:
            if requests.get(self.__webhooks).status_code == 401:
                raise Notifier.__AuthError('Invalid Webhook')
        except exceptions.ConnectionError as err:
            print('HTTPS Connection Error - Unable to reach the destination')
            exit(1)
        except Notifier.__AuthError as ty_err:
            print(ty_err)
            exit(1)
        except requests.models.MissingSchema as ms_err:
            print(ms_err)
            exit(1)

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
        except exceptions.ConnectionError as cer:
            print(cer)
            exit(1)

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
            exit(1)
