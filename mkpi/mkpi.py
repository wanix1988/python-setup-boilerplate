#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
@author Linwei.Wang
@email wenix@live.cn
@date 2018/06/19
'''

import os
import shutil

def create_project(args):
    project_name = args.name
    if project_name:
        cwd = os.getcwd()
        try:
            os.mkdir(os.path.join(cwd, project_name))
        except OSError as err:
            print('%s directory has existed!' % project_name)
        basedir = os.path.dirname(os.path.abspath(__file__)),
        print('basedir:', basedir[0])
        files = os.listdir(os.path.join(basedir[0], 'template'))
        for f in files:
            dst = f
            if f.endswith('.tpl'):
               dst = f[:-4]
            shutil.copy(os.path.join(basedir, 'template', f),
                        os.path.join(cwd, project_name, dst))
        print('%s has been created' % project_name)
