#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import setuptools

with open('README.md', 'r', encoding='UTF-8') as df:
    long_description = df.read()
    
setuptools.setup(
    name = "mkpi",
    version = "0.1",
    author = "Linwei Wang",
    author_email = "wenix@live.cn",
    description = "make python project setuptools template",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "",
    packages = setuptools.find_packages(),
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'mkpi=mkpi:main'
        ]
    },
    classifiers = (
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT Licens",
        "Operating System :: OS Independent",
    )
)