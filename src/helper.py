#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import urllib.request
import logging

log = logging.getLogger('argus.helper')

def retrieve_full_url(url):
    s = ''
    try:
        f = urllib.request.urlopen(url)
        s = f.readall().decode('utf8')
    except IOError as e:
        if hasattr(e, 'reason'):
            log.error('an error occured while fetching url (reason: {}).'.format(e.reason))
        elif hasattr(e, 'code'):
            log.error('The server couldn\'t fulfill the request (error code: {}).'.format(e.code))
    except UnicodeDecodeError as e:
        log.error('an unicode decode error has appeared: {}'.format(e.reason))
        
    return s

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
