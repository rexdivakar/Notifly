"""Slack-API call wrapper"""


import slack
from slack.errors import SlackApiError


class Notifier:
    def __init__(self, token, channel):
        """
        Initialize the slack webclient instance using API

        :argument token: -> API token [Mandatory]
        :argument channel: -> Post's the notification to the corresponding channel [default = #general]

        :return: the output of slack API_test which verify the Authentication protocol
        """
        self.__client = slack.WebClient(token = token)
        self.__channel = channel

        try:
            self.__client.api_test()['ok']
        except SlackApiError as api_err:
            print(f"Got an error: {api_err.response['error']}")
            exit(1)

    def send_message(self, msg):  #TODO  Add unicode check
        """
        send_message -> function to post message to the slack channel

        :argument msg: -> Enter your message to post
        :return: response to the message post
        """
        try:
            return self.__client.chat_postMessage(channel = self.__channel, text = msg)
        except SlackApiError as api_err:
            print(f"Got an error: {api_err.response['error']}")
            exit(1)

    def send_image(self, file_path):
        """
        send_image -> function to post an image to the slack channel

        :argument file_path: -> enter the path of the file to be sent
        :return: response to the message post
        """
        try:
            return self.__client.files_upload(file = file_path,  channels = self.__channel)
        except FileNotFoundError as fl_err:
            print(fl_err)
