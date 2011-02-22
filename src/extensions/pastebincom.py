#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import BaseExtension
import urllib.request
import re
import config
import helper

class Extension(BaseExtension.BaseExtension):
    '''Extension for pastebin.com'''
    
    def __init__(self, queue):
        BaseExtension.BaseExtension.__init__(self)  #init thread
        self.len_archive = 2009                     #nr. of available pastbin.com archives
        self.base_url = 'http://pastebin.com'
        self.pattern = re.compile('http://pastebin.com/([a-zA-Z0-9]{8})')
        self.queue = queue                          #global queue to put the junk in
        self.config = config.Config()               #config
    
    def run(self):
        '''perform data harvesting

        1. generate a list of url's to visit
        2. visit each url
        3. put data in queue {url = link to post, data = raw data}'''
        for url in self._generate_url():
            dd = {'url' : url}  #new data dictionary
            dd['data'] = helper.retrieve_full_url(url)

            self.queue.put(dd)

    def _generate_url(self):
        '''yield pastebin url's'''
        amount = 0
        index = 0
        cache = []
        for nr in range(1, self.len_archive):
            self._update_cache(cache, self._harvest_archive(nr))
            while index < len(cache):
                if amount < self.config.max_urls_per_pastebin:
                    yield '{}/{}'.format(self.base_url, cache[index])
                    index += 1
                    amount += 1
                else: 
                    return

    def _harvest_archive(self, nr):
        '''harvest pastebin archive page <nr> and return pastebin id's'''
        f = urllib.request.urlopen('{}/archive/{}'.format(self.base_url, nr))
        l = self.pattern.findall(f.readall().decode('utf8'))
        return list(set(l))

    def _update_cache(self, cache, items):
        '''update the cache with the given list of items if an item isn't present in the cache.''' 
        for elem in items:
            if elem not in cache:
                cache.append(elem)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
