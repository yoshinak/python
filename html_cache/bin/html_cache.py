#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5, os, os.path
import urllib

class HtmlCache(object):
    # get HTML from cache, or net.

    # Calcurate hex hash or bubble.
    def calcurate_hash(self, url):
        return md5.new(url).hexdigest()

    # Set top directory of cache.
    def set_cache_top(self, cache_top):
        self.cache_top = cache_top

    # Create unique path of URL.
    def create_path(self, url):
        if self.cache_top is None:
            raise ValueError('cache_top is not defined.')
        return os.path.abspath(os.path.join(self.cache_top, self.calcurate_hash(url)))

    # Get html from cache.
    def get_cache(self, url):
        f = open(self.create_path(url), 'r')
        return f.read()

    # Get html from net.
    def get_html_from_net(self, url):
        page = urllib.urlopen(url).read()
        file_path = self.create_path(url)
        f = open(file_path, 'w+')
        f.write(page)
        return page
    
    # Check if directory/file exists.
    def get_html(self, url):
        cache_file_path = self.create_path(url)
        if os.path.isfile(cache_file_path):
            page = self.get_cache(url)
        else:
            page = self.get_html_from_net(url)
        return page
