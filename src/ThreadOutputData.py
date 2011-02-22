#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import threading

class ThreadOutputData(threading.Thread):
    '''process data'''
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            item = self.out_queue.get()
            print('url: {} ++ data: {}'.format(item['url'], item['data']))
            self.out_queue.task_done()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
