import slack
from slack.errors import SlackApiError, SlackRequestError


class Notifier:
    """Slack-API call wrapper"""
    def __init__(self, token, channel):
        self.__client = slack.WebClient(token = token)
        self.__channel = channel

        try:
            self.__client.api_test()['ok']
        except SlackApiError as api_err:
            print(f"Got an error: {api_err.response['error']}")
            exit(1)

    def send_message(self, msg):  #TODO  Add unicode check
        try:
            return self.__client.chat_postMessage(channel = self.__channel, text = msg)
        except SlackApiError as api_err:
            print(f"Got an error: {api_err.response['error']}")
            exit(1)

    def send_image(self, channel, file_path):
        try:
            return self.__client.files_upload(file = file_path,  channels = channel)
        except FileNotFoundError as fl_err:
            print(fl_err)
