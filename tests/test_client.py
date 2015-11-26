# coding: utf-8
import unittest

from doaj.client import Client


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