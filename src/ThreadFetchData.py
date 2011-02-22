#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import threading
import urllib.request

class ThreadFetchData(threading.Thread):
    '''Fetch content of a URL'''
    def __init__(self, url_queue, junk_queue):
        threading.Thread.__init__(self)
        self.url_queue = url_queue
        self.junk_queue = junk_queue

    def run(self):
        while True:
            url = self.url_queue.get()
            
            try:
                f = urllib.request.urlopen(url)
                s = f.readall().decode('utf8')
                self.junk_queue.put(s)
            except IOError as e:
                if hasattr(e, 'reason'):
                    print('an error occured while fetching url (reason: {}).'.format(e.reason))
                elif hasattr(e, 'code'):
                    print('The server couldn\'t fulfill the request (error code: {}).'.format(e.code))
            except UnicodeDecodeError as e:
                print('an unicode decode error has appeared: {}'.format(e.reason))

            self.url_queue.task_done()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
