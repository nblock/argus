#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

from abc import ABCMeta, abstractmethod
import threading

class BaseExtension(threading.Thread, metaclass=ABCMeta):
    '''BaseExtension -- abstract Extension class'''
    
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name,
                                  verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    @abstractmethod
    def run(self):
        '''fetch pastebin data and save it in a queue'''
        pass

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
