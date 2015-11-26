# coding: utf-8
import requests

VERSION = 'v1'

class Client(object):

    def __init__(self, usertoken=None):
        self.token = usertoken
        self.url = "https://doaj.org/api/%s/" % VERSION

    def ping(self):

        response = self.request("swagger.json", raw=True)

        if response.status_code == 200:
            return True

        return False

    def request(self, querystring, raw=False):
        
        url = self.url+querystring

        response = requests.get(url)

        if raw:
            return response

        return response.json()
