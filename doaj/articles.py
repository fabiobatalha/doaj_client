# coding: utf-8

from doaj.client import Client


class Articles(Client):

    def search(query, page, pagesize, sort):
        """
        query must be a valid lucene query
        """
        pass

