#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import BaseExtension
import urllib.request
import re
import time

class Extension(BaseExtension.BaseExtension):
    '''Extension for pastebin.com'''
    
    def __init__(self, testqueue):
        BaseExtension.BaseExtension.__init__(self)
        self.len_archive = 200
        self.base_url = 'http://pastebin.com'
        self.pattern = re.compile('http://pastebin.com/([a-zA-Z0-9]{8})')
        self.q = testqueue
    
    def run(self):
        for i in range(100):
            self.q.put('iiiiii {}'.format(i))
            time.sleep(1)
        print('test')

    def _generate_url(self, max = 100):
        '''yield pastebin url's

        max -- maximum amount of url's to yield'''
        amount = 0
        index = 0
        cache = []
        for nr in range(1, self.len_archive):
            self._update_cache(cache, self._harvest_archive(nr))
            while index < len(cache):
                if amount < max:
                    yield '{}/{}'.format(self.base_url, cache[index])
                    index += 1
                    amount += 1
                else: 
                    return

    def _harvest_archive(self, nr):
        '''harvest pastebin archive page <nr> and return pastebin id's'''
        f = urllib.request.urlopen('{}/archive/{}'.format(self.base_url, 2))
        l = self.pattern.findall(f.readall().decode('utf8'))
        return list(set(l))

    def _update_cache(self, cache, items):
        '''update the cache with the given list of items if an item isn't present in the cache.''' 
        for elem in items:
            if elem not in cache:
                cache.append(elem)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
