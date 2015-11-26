# coding: utf-8
import unittest

from doaj.client import Client
from doaj.articles import Articles
from doaj.journals import Journals
from doaj.applications import Applications


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


class ApplicationsTest(unittest.TestCase):

    def setUp(self):
        self.ap = Applications(usertoken='usertk')

    def test_instantiate_without_token(self):
        
        ap = Applications()
        with self.assertRaises(ValueError):
            ap.search('id:xxx')

    def test_get_application_not_available(self):
        response = self.ap.get('not available')

        self.assertEqual(response['status'], 'not_found')

    def test_search_invalid_page_size(self):
        
        with self.assertRaises(ValueError):
            [x for x in self.ap.search('issn:1806-9940', pagesize='invalid')]

    def test_search_invalid_page_size_1(self):
        """
        not between 10 and 100.
        """
        with self.assertRaises(ValueError):
            [x for x in self.ap.search('issn:1806-9940', pagesize=9)]

    def test_search_invalid_page_size_2(self):
        """
        not between 10 and 100.
        """
        with self.assertRaises(ValueError):
            [x for x in self.ap.search('issn:1806-9940', pagesize=101)]


class JournalsTest(unittest.TestCase):

    def setUp(self):
        self.jn = Journals()

    def test_get_journal(self):
        response = self.jn.get('022bf3ad951c4c5fa77a8279a59c437e')

        self.assertTrue('bibjson' in response)

    def test_get_journal_not_available(self):
        response = self.jn.get('not available')

        self.assertEqual(response['status'], 'not_found')

    def test_search_invalid_page_size(self):
        
        with self.assertRaises(ValueError):
            [x for x in self.jn.search('issn:1806-9940', pagesize='invalid')]

    def test_search_invalid_page_size_1(self):
        """
        not between 10 and 100.
        """
        with self.assertRaises(ValueError):
            [x for x in self.jn.search('issn:1806-9940', pagesize=9)]

    def test_search_invalid_page_size_2(self):
        """
        not between 10 and 100.
        """
        with self.assertRaises(ValueError):
            [x for x in self.jn.search('issn:1806-9940', pagesize=101)]

    def test_search(self):

        journals = [x for x in self.jn.search('id:022bf3ad951c4c5fa77a8279a59c437e')]

        self.assertEqual(1, len(journals))

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

    def test_search(self):

        articles = [x for x in self.ac.search('id:255723f2f2374f1fbb8865eeb044c9d2')]

        self.assertEqual(1, len(articles))

