"""
Copyright (c) 2016 Jet Propulsion Laboratory,
California Institute of Technology.  All rights reserved
"""
from setuptools import setup

__version__ = '0.1'

setup(
    name='ningesterproto',
    version=__version__,
    url="https://github.com/aist-oceanworks",

    author="Team Nexus",

    description="Protobufs used while ingesting NEXUS tiles.",

    packages=['ningesterproto'],
    platforms='any',

    install_requires=[
        'protobuf'
    ],

    classifiers=[
        'Development Status :: 1 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ]
)
