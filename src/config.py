#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

class Config():
    '''configuration parameters for argus'''
    #TODO: 
    # -add support for config file
    # - validation
    # - commandline parameters

    #max url's per pastebin
    max_urls_per_pastebin = 4

    #how many threads should be used for fetching
    #TODO: re-implement
    fetch_threads = 2

    #how many threads should be used for datamining
    datamine_threads = 1
    
    #extension directory
    extensions_directory = 'extensions/'
    
    #rules directory
    rules_directory = 'rules.d/'

    #http timeout in seconds (global)
    http_timeout = 5

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
