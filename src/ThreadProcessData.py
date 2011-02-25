#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import threading
import re

class ThreadProcessData(threading.Thread):
    '''process data'''
    def __init__(self, junk_queue, out_queue, rules):
        threading.Thread.__init__(self)
        self.junk_queue = junk_queue
        self.out_queue = out_queue
        self.rules = rules

    def run(self):
        while True:
            junk = self.junk_queue.get()

            for k, v in self.rules.items():
                #iterate over rules for group k
                for val in v:
                    match = re.search(val, junk['data'], re.IGNORECASE)
                    if match:
                        self.out_queue.put(junk)

            self.junk_queue.task_done()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
