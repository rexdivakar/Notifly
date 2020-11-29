"""Slack-API call wrapper"""

import slack
from slack.errors import SlackApiError
from notifly.tf_notifier import TfNotifier


class Notifier(TfNotifier):
    def __init__(self, token, channel='general'):
        """
        Initialize the slack webclient instance using API.

        Args:
            token (string): API token [Mandatory].
            channel (string): Post's the notification to it's corresponding channel [default = #general].
        Returns:
            The output of slack API_test which verify the Authentication protocol.
        Raises:
            SlackApiError.
        """
        self.__client = slack.WebClient(token=token)
        self.__channel = channel

        try:
            self.__client.api_test()['ok']
        except SlackApiError as api_err:
            print(f"Got an error: {api_err.response['error']}")
            exit(1)

    def send_message(self, msg) -> object:
        """
        Function to post message to the slack channel.

        Args:
            msg (string): Enter your message to post.
        Returns:
            Outputs the response of message on post operation.
        Raises:
            SlackApiError
        """
        try:
            return self.__client.chat_postMessage(channel=self.__channel, text=msg)
        except SlackApiError as api_err:
            print(f"Got an error: {api_err.response['error']}")
            exit(1)

    def send_file(self, file_path) -> object:
        """
        Function to post an file to the slack channel.

        Args:
            file_path (string): Enter the path of the file to be sent.
        Returns:
            Outputs the response of message on post operation.
        Raises:
                FileNotFoundError
        """
        try:
            return self.__client.files_upload(file=file_path, channels=self.__channel)
        except FileNotFoundError as fl_err:
            print(fl_err)
