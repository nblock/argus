#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import pkgutil
import imp
import os
import sys
import config

c = config.Config()

class ExtensionManager:
    '''ExtensionManager -- process extensions'''

    extensions = {}

    def __init__(self, folder = c.extensions_directory):
        '''add every extension to extensions dict'''
        plugin_path = []
        plugin_path.append(os.path.join(os.path.abspath('.'), folder))
        sys.path.append(plugin_path)

        for loader, name, ispkg in pkgutil.iter_modules(plugin_path):
            file, pathname, desc = imp.find_module(name, plugin_path)
            mod = imp.load_module(name, file, pathname, desc)

            #load only if Extensions is present
            if hasattr(mod, 'Extension'):
                self.extensions[name] = mod

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
