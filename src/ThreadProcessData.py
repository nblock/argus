#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import threading

class ThreadProcessData(threading.Thread):
    '''process data'''
    def __init__(self, junk_queue):
        threading.Thread.__init__(self)
        self.junk_queue = junk_queue

    def run(self):
        while True:
            #grabs host from queue
            junk = self.junk_queue.get()

            print(junk[:10])
            self.junk_queue.task_done()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
