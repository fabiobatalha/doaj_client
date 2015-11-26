# coding: utf-8
import requests

VERSION = 'v1'

class Client(object):

    def __init__(self, usertoken=None):
        self.token = usertoken
        self.api_url = 'https://doaj.org/api/%s/' % VERSION

    def ping(self):

        url = self.api_url+'swagger.json'
        response = self.request_get(url, raw=True)

        if response.status_code == 200:
            return True

        return False

    def request_get(self, url, payload=None, raw=False):

        if not isinstance(payload, dict):
            payload = {}

        response = requests.get(url, params=payload)

        if raw:
            return response

        return response.json()
