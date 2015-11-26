# coding: utf-8
import requests
from functools import wraps

VERSION = 'v1'
PAGESIZE = 10

def must_have_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not args[0].token:
            raise ValueError('You must specify a valid user token to use this method')
        result = func(*args, **kwargs)
        return result
    return wrapper

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
