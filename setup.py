#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name            = 'django-verified-email-field',
    version         = '1.9.0',
    description     = 'Simple model and form field to get verified email',
    author          = 'Jakub Dorňák',
    author_email    = 'jakub.dornak@misli.cz',
    license         = 'BSD',
    url             = 'https://github.com/misli/django-verified-email-field',
    packages        = find_packages(),
    include_package_data = True,
    install_requires = [
    ],
    classifiers     = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Czech',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
