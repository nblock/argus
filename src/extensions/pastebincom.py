#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import BaseExtension
import urllib.request
import re

#TODO: caching yields double entries...
class Extension(BaseExtension.BaseExtension):
    '''Extension for pastebin.com'''
    
    def __init__(self):
        self.len_archive = 200
        self.base_url = 'http://pastebin.com'
        self.pattern = re.compile('http://pastebin.com/([a-zA-Z0-9]{8})')

    def generate_url(self, max = 100):
        '''yield pastebin url's

        max -- maximum amount of url's to yield'''
        amount = 0
        for nr in range(1, self.len_archive):
            cache = self._harvest_archive(nr)
            while len(cache) > 0:
                if amount < max:
                    yield '{}/{}'.format(self.base_url, cache[0])
                    del cache[0]
                    amount += 1
                else: 
                    return

    def _harvest_archive(self, nr):
        '''harvest pastebin archive page <nr> and return pastebin id's'''
        f = urllib.request.urlopen('{}/archive/{}'.format(self.base_url, 2))
        l = self.pattern.findall(f.readall().decode('utf8'))
        return list(set(l))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
