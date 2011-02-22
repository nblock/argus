#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import urllib.request

def retrieve_full_url(url):
    try:
        f = urllib.request.urlopen(url)
        s = f.readall().decode('utf8')
        return s
    except IOError as e:
        if hasattr(e, 'reason'):
            print('an error occured while fetching url (reason: {}).'.format(e.reason))
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request (error code: {}).'.format(e.code))
    except UnicodeDecodeError as e:
        print('an unicode decode error has appeared: {}'.format(e.reason))

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
