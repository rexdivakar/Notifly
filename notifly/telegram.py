""" Telegram Wrapper"""

import json
import os
import sys
import requests
from notifly.tf_notifier import TfNotifier


class Notifier(TfNotifier):
    def __init__(self, token, dir_download= './downloads'):
        """
        Initialize the telegram client using tokens to access the HTTP API

        Args:
            token (string): API token [Mandatory].
        Args:
            dir_download (string): -> Storage location for dumping payload [default = "./downloads"]
        """
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        self.file_url = "https://api.telegram.org/file/bot{}/".format(token)
        self.dirDownloads = dir_download

    def __get_updates(self, offset=0, timeout=10):
        """
        Get the latest updates as json file

        Args:
            offset (int): default value 0
            timeout (int): Timeout for the request post (default value 10)
        Returns:
            The json results
        Raises:
            TimeoutError
        """
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        try:
            return resp.json()['result']
        except KeyError:
            print('TimeoutError')
            sys.exit(1)
        except requests.exceptions.ConnectionError as err:
            print('HTTPS Connection Error - Unable to reach the destination')

    def __chat_id_response(self) -> int:
        """
        Fetches the latest chat id from the client

        Returns:
            The latest chat-id of the client
        Raises:
            TimeoutError
        """
        try:
            fetch_updates = self.__get_updates()
            return fetch_updates[0]['message']['chat']['id']
        except TimeoutError as tm_err:
            print(tm_err)
            sys.exit(1)

    def send_message(self, msg, notification=False) -> object:
        """
        Function to send message

        Args:
            msg (string): Enter the message to post
            notification (bool): Disable_Notification (default=False)
        Returns:
            The status_code of the post operation (send_message)
        Raises:
            IndexError
        """
        try:
            method = 'sendMessage'
            params = {'chat_id': self.__chat_id_response(), 'text': msg,
                      'parse_mode': 'HTML', 'disable_notification': notification}
            return requests.post(self.api_url + method, params)
        except IndexError:
            print('Time out error')
            sys.exit(1)
        except requests.exceptions.ConnectionError as err:
            print('HTTPS Connection Error - Unable to reach the destination')
            sys.exit(1)

    def send_image(self, img_path) -> object:
        """
        Function to send image via telegram

        Args:
            img_path (basestring): Enter the file_path to send the image file
        Returns:
            The status_code of the post operation (send_image)
        Raises:
            FileNotFoundError, InvalidFormatError
        """
        method = 'sendPhoto?' + 'chat_id=' + str(self.__chat_id_response())
        if img_path[-4:] not in ['.jpg', '.png']:
            print('Invalid File Format, please use .jpg or .png format')
            sys.exit(1)
        try:
            files = {'photo': open(img_path, 'rb')}
            return requests.post(self.api_url + method, files = files)
        except FileNotFoundError as fl_err:
            print(fl_err)
            sys.exit(1)
        except requests.exceptions.ConnectionError as err:
            print('HTTPS Connection Error - Unable to reach the destination')
            sys.exit(1)

    def send_file(self, file_path) -> object:
        """
        Function to send documents via telegram

        Args:
            file_path (basestring): Enter the file_path to send the image file
        Returns:
            The status_code of the post operation (send_document)
        Raises:
            FileNotFoundError, TimeoutError
        """
        method = 'sendDocument?' + 'chat_id=' + str(self.__chat_id_response())
        try:
            files = {'document': open(file_path, 'rb')}
            return requests.post(self.api_url + method, files = files)
        except FileNotFoundError as fn_err:
            print(fn_err)
            sys.exit(1)
        except TimeoutError as tm_err:
            print(tm_err)
            sys.exit(1)
        except requests.exceptions.ConnectionError as err:
            print('HTTPS Connection Error - Unable to reach the destination')
            sys.exit(1)

    def session_dump(self) -> json:
        """
        Function to Dump all the data from the telegram client during the current session

        Returns:
            Dumps the session details in the form of json file.
        Raises:
            IOError
        """
        resp = self.__get_updates()
        try:
            if not os.path.exists(self.dirDownloads):
                os.mkdir(self.dirDownloads)
            local_path = os.path.join(self.dirDownloads, 'session_dump.json')

            with open(local_path, 'w+', encoding='utf-8') as outfile:
                json.dump(resp, outfile)
        except IOError as io_err:
            print(io_err)
            sys.exit(1)
