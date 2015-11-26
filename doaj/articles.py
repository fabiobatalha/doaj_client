# coding: utf-8
from doaj.client import Client, PAGESIZE

class Articles(Client):

    endpoint = "articles/"
    search_endpoint = "search/articles/"

    def search(self, query, sort=None, pagesize=PAGESIZE):
        """
        query must be a valid lucene query
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


    def get(self, article_id):
        """
        Retrieve one article related to the given article identification.
        """
        url = self.api_url+self.endpoint+article_id

        return self.request_get(url)