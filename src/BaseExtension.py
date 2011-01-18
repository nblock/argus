#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

from abc import ABCMeta, abstractmethod

class BaseExtension(metaclass=ABCMeta):
    '''BaseExtension -- abstract Extension class'''

    @abstractmethod
    def generate_url(self):
        '''yield a new target url'''
        pass

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
