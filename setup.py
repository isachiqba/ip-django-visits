#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os
import counter

setup(
    name='counter',
    version=counter.get_version(),
    description="Visit counter for Django",
    long_description=open('README.rst', 'r').read(),
    keywords='django, visit, counter, visitors',
    author='Jesús Espino García',
    author_email='jespinog at gmail dot com',
    url='https://bitbucket.org/jespino/simplecounter',
    license='LGPL',
    package_dir={'counter': 'counter'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
        "Topic :: System :: Monitoring",
        "Topic :: Utilities",
    ]
)
