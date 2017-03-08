#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from setuptools import setup, find_packages

setup(
    name            = 'django-verified-email-field',
    version         = '1.2.0',
    description     = 'Simple model and form field to get verified email',
    author          = 'Jakub Dorňák',
    author_email    = 'jakub.dornak@misli.cz',
    license         = 'BSD',
    url             = 'https://github.com/misli/django-verified-email-field',
    packages        = find_packages(),
    install_requires=[
    ],
    classifiers     = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
