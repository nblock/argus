#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##
# project: this file is part of argus
# author: notizblock <nblock@archlinux.us>
# license: GPLv3

import config
import os
import glob

c = config.Config()

class RulesManager:
    '''RulesManager -- process rules in rules_directory'''
        
    def __init__(self, folder = c.rules_directory, extension='.rules'):
        '''read each .rules file in rules_directory and return ready a rules dict'''
        self.rules = {}
        self.rules_path = os.path.join(os.path.abspath('.'), folder)
        self.extension = extension

    def get_rules_dict(self):
        '''get a rules dict

        fmt: {filename : [list of rules per file, ],} or an empty dict of no rules are present
        -files without .rules suffix will be ignored
        -empty lines or lines starting with # will be ignored 
        '''

        for infile in glob.glob(os.path.join(self.rules_path, ''.join(('*', self.extension)))):
            key = os.path.basename(infile)[:-len(self.extension)]
            self.rules[key] = []

            with open(infile, 'r', encoding='utf8') as f:
                for line in f:
                    line = line.strip()
                    if len(line) == 0 or line.startswith('#'):
                        pass
                    else:
                        self.rules[key].append(line)

        return self.rules

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 smartindent autoindent 
