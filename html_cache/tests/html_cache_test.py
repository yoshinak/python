#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../bin'
import_dir = os.path.abspath(os.path.join(testdir, srcdir))
print(import_dir)
sys.path.insert(0, import_dir)

from html_cache import HtmlCache
import unittest

class HtmlCacheTestCase(unittest.TestCase):
    TEST_URL = 'http://foo.bar/hoge'
    TEST_URL_DL = 'https://google.com'

    def setup_cache_exists(self):
        html_cache = HtmlCache()
        cache_top = os.path.abspath(os.path.join(testdir, '../tests/test_data'))
        html_cache.set_cache_top(cache_top)
        return html_cache

    def test_has_train_data(self):
        # Prepare
        html_cache = self.setup_cache_exists()
        url = self.TEST_URL
        # Execute
        actual = html_cache.calcurate_hash(url)
        print "actual=" + actual
        # Assert
        self.assertNotEqual(actual, url)

    def test_create_path(self):
        # Prepare
        html_cache = self.setup_cache_exists()
        url = self.TEST_URL
        # Execute
        actual = html_cache.create_path(url)
        print "actual=" + actual
        # Assert
        self.assertNotEqual(actual, url)

    def test_get_cache(self):
        # Prepare
        html_cache = self.setup_cache_exists()
        url = self.TEST_URL
        # Execute
        actual = html_cache.get_cache(url)
        # Assert
        self.assertIsNotNone(actual)
        if not "html" in actual:
            self.fail("Not html.")

    def test_get_html_from_net(self):
        # Prepare/Execute
        html_cache = self.setup_cache_exists()
        url = self.TEST_URL_DL

        cache_file_path = html_cache.create_path(url)
        if os.path.isfile(cache_file_path):
            os.remove(cache_file_path)

        # Execute
        html_cache.get_html_from_net(url)

        # Assert
        if not os.path.isfile(cache_file_path):
            self.fail("No html.")

        f = open(html_cache.create_path(url), 'r')
        actual_page = f.read()
        if not "html" in actual_page:
            self.fail("Not html.")
        print "actual_page=" + actual_page

        # Teardown
        if os.path.isfile(cache_file_path):
            os.remove(cache_file_path)

    def test_get_html_cache_exists(self):
        # Prepare
        html_cache = self.setup_cache_exists()
        url = self.TEST_URL_DL

        cache_file_path = html_cache.create_path(url)
        if os.path.isfile(cache_file_path):
            os.remove(cache_file_path)

        # Prepare cache
        html_cache.get_html_from_net(url)

        # Assert preparation
        if not os.path.isfile(cache_file_path):
            self.fail("No html.")

        # Execute
        actual = html_cache.get_html(url)

        # Assert
        if not "html" in actual:
            self.fail("Not html.")
        print "actual=" + actual

        # Teardown
        if os.path.isfile(cache_file_path):
            os.remove(cache_file_path)

    def test_get_html_cache_not_exists(self):
        # Prepare
        html_cache = self.setup_cache_exists()
        url = self.TEST_URL_DL

        cache_file_path = html_cache.create_path(url)
        if os.path.isfile(cache_file_path):
            os.remove(cache_file_path)

        # Assert preparation
        if os.path.isfile(cache_file_path):
            self.fail("Cache exists.")

        # Execute
        actual = html_cache.get_html(url)

        # Assert
        if not "html" in actual:
            self.fail("Not html.")
        print "actual=" + actual

        # Teardown
        if os.path.isfile(cache_file_path):
            os.remove(cache_file_path)
