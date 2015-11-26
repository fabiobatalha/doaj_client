# coding: utf-8
import unittest

from doaj.client import Client
from doaj.articles import Articles


class ClientTest(unittest.TestCase):

    def setUp(self):

        self.cl = Client()

    def test_instantiate(self):
        self.assertEqual(self.cl.token, None)

    def test_instantiate_with_token(self):
        cl = Client(u'usertk')
        self.assertEqual(cl.token, u'usertk')

    def test_ping(self):
        self.assertTrue(self.cl.ping(), True)

class ArticlesTest(unittest.TestCase):

    def setUp(self):
        self.ac = Articles()

    def test_get_article(self):
        response = self.ac.get('255723f2f2374f1fbb8865eeb044c9d2')

        self.assertTrue('bibjson' in response)

    def test_get_article_not_available(self):
        response = self.ac.get('not available')

        self.assertEqual(response['status'], 'not_found')

    def test_search_invalid_page_size(self):
        
        with self.assertRaises(ValueError):
            [x for x in self.ac.search('issn:1806-9940', pagesize='invalid')]

    def test_search_invalid_page_size_1(self):
        """
        not between 10 and 100.
        """
        with self.assertRaises(ValueError):
            [x for x in self.ac.search('issn:1806-9940', pagesize=9)]

    def test_search_invalid_page_size_2(self):
        """
        not between 10 and 100.
        """
        with self.assertRaises(ValueError):
            [x for x in self.ac.search('issn:1806-9940', pagesize=101)]
