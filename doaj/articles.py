# coding: utf-8

from doaj.client import Client


class Articles(Client):

    endpoint = "articles/"
    search_endpoint = "search/articles/"

    def search(self, query, page, pagesize, sort):
        """
        query must be a valid lucene query
        """
        pass

    def get(self, article_id):
        """
        Retrieve one article related to the given article identification.
        """
        url = self.api_url+self.endpoint+article_id

        return self.request_get(url)