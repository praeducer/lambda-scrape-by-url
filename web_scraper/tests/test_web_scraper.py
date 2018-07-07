from unittest import TestCase
from web_scraper import *


class TestWebScraper(TestCase):
    def test_has_correct_return_type(self):
        s = scrape_by_url('http://www-03.ibm.com/press/us/en/pressrelease/53622.wss')
        self.assertTrue(isinstance(s, str))
        lst = crawl_by_url('http://www-03.ibm.com/press/us/en/pressrelease/53622.wss')
        self.assertTrue(type(lst) is list)
        self.assertFalse(isinstance(lst, str))
        self.assertTrue(all(isinstance(n, str) for n in lst))
        lst = crawl_by_keyword('IBM')
        self.assertTrue(type(lst) is list)
        self.assertFalse(isinstance(lst, str))
        self.assertTrue(all(isinstance(n, str) for n in lst))

    def test_result_is_none(self):
        value = scrape_by_url(None)
        self.assertIsNone(value)
        value = scrape_by_url(0)
        self.assertIsNone(value)
        value = scrape_by_url(1)
        self.assertIsNone(value)
        value = scrape_by_url(True)
        self.assertIsNone(value)
        value = scrape_by_url(False)
        self.assertIsNone(value)
        value = scrape_by_url([])
        self.assertIsNone(value)
        value = scrape_by_url(["http://www-03.ibm.com/press/us/en/pressrelease/53622.wss"])
        self.assertIsNone(value)
        value = scrape_by_url("")
        self.assertIsNone(value)
        value = scrape_by_url("www")
        self.assertIsNone(value)
        value = scrape_by_url(".com")
        self.assertIsNone(value)
        value = scrape_by_url("http://")
        self.assertIsNone(value)
        value = crawl_by_url(None)
        self.assertIsNone(value)
        value = crawl_by_url(0)
        self.assertIsNone(value)
        value = crawl_by_url(1)
        self.assertIsNone(value)
        value = crawl_by_url(True)
        self.assertIsNone(value)
        value = crawl_by_url(False)
        self.assertIsNone(value)
        value = crawl_by_url([])
        self.assertIsNone(value)
        value = crawl_by_url(["http://www-03.ibm.com/press/us/en/pressrelease/53622.wss"])
        self.assertIsNone(value)
        value = crawl_by_url("")
        self.assertIsNone(value)
        value = crawl_by_url("www")
        self.assertIsNone(value)
        value = crawl_by_url(".com")
        self.assertIsNone(value)
        value = crawl_by_url("http://")
        self.assertIsNone(value)
