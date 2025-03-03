#!/usr/bin/python

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pycky",
    version = "0.1.2",
    author = "Joseph Kern",
    author_email = "no@reply.com",
    description = ("Search for python module dependencies using the "
                                   "Abstract Source Tree (AST)"),
    license = "BSD",
    keywords = "AST analysis developer",
    url = "http://packages.python.org/pyck",
    packages=['pycky', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Code Analysis",
        "License :: OSI Approved :: BSD License",
    ],
    scripts=[
        'bin/pycky'
        ],
)
