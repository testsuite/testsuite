#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('CHANGELOG.rst').read().replace('.. :changelog:', '')

config = {
    'name': 'testsuite',
    'version': '0.1.0',
    'description': 'Testsuite is a command line tool that helps you manage your tests.',
    'long_description': readme + '\n\n' + history,
    'author': 'Omer Katz',
    'author_email': 'omer.drow@gmail.com',
    'url': 'https://github.com/testsuite/testsuite',
    'packages': [
        'testsuite',
    ],
    'package_dir': {'testsuite': 'testsuite'},
    'include_package_data': True,
    'install_requires': [
    ],
    'setup_requires': ['setuptools'],
    'tests_requires': ['nose2>=0.4.7', 'nose2-cov==1.04a', 'behave>=1.2.3', 'mock>=1.0.1', 'forbiddenfruit>=0.1.0',
                       'what>=0.4.4'],
    'test_suite': 'nose2.collector.collector',
    'license': 'BSD3',
    'zip_safe': False,
    'keywords': 'testsuite',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: PyPy',
    ],
}

setup(
    **config
)