# coding: utf-8
from doaj.client import Client, PAGESIZE, must_have_token

class Applications(Client):

    endpoint = "applications/"
    search_endpoint = "search/applications/"

    @must_have_token
    def search(self, query, sort=None, pagesize=PAGESIZE):
        """
        query must be a valid lucene query
        sort must be field:[asc|desc]
        """

        try:
            int(pagesize)
        except:
            raise ValueError('pagesize must be integer')

        if pagesize > 100 or pagesize < 10:
            raise ValueError('pagesize must be between 10 and 100')

        page = 1
        payload = {'pageSize': pagesize, 'page': page}
        while True:
            url = self.api_url+self.search_endpoint+query

            response = self.request_get(url, payload=payload)

            if len(response.get('results', [])) == 0:
                break

            for item in response.get('results'):
                yield item

            payload['page'] += 1


    @must_have_token
    def get(self, journal_id):
        """
        Retrieve one journal related to the given journal identification.
        """
        url = self.api_url+self.endpoint+journal_id

        return self.request_get(url)