#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
@author Linwei.Wang
@email wenix@live.cn
@date 2018/06/19
'''

import 
import argparse

def create_project(name):
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make Python Project Setuptools Template.')
    parser.add_argument('--name', required=True, help='specify project\'s name')
    args = parser.parse_args()
    project_name = args.name
    print(project_name)
