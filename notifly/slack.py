import requests
import json


class Notifier:
    def __init__(self, webhooks):
        self.__webhooks = webhooks

    def send_message (self, msg):
        data = {'text': msg, 'response_type': 'in_channel'}
        response = requests.post (self.__webhooks, data = json.dumps (data),
                                  headers = {'Content-Type': 'application/json'})

    # def send_file(self, payload):
    #     payload_json = json.dumps(payload)
    #     data = {"payload": payload_json , 'response_type': 'in_channel'}
    #
    #     response = requests.post(self.__webhooks, data = json.dumps (data),
    #                               headers = {'Content-Type': 'application/json'})


