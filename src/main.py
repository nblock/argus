#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import ExtensionManager
import ThreadFetchData
import ThreadProcessData
import queue
import socket

def main():
    url_queue = queue.Queue()
    junk_queue = queue.Queue()
    cal_queue = queue.Queue()
    socket.setdefaulttimeout(10) #apply global timeout
    
    #spawn some fetchers
    for i in range(2):
        t = ThreadFetchData.ThreadFetchData(url_queue, junk_queue)
        t.setDaemon(True)
        t.start()
    
    em = ExtensionManager.ExtensionManager()
    lext = [mod.Extension() for mod in em.extensions.values()]

    for ex in lext:
        for url in ex.generate_url(10):
            url_queue.put(url)

    #spawn some datamining threads
    for i in range(1):
        dt = ThreadProcessData.ThreadProcessData(junk_queue)
        dt.setDaemon(True)
        dt.start()
    
    #wait until data processing has been finished
    url_queue.join()
    junk_queue.join()


if __name__ == '__main__':
    main()

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
