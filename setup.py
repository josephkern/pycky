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
    name = "pyck",
    version = "0.0.1",
    author = "Joseph Kern",
    author_email = "jkern@semafour.net",
    description = ("Search for python module dependencies using the "
                                   "Abstract Source Tree (AST)"),
    license = "BSD",
    keywords = "AST analysis developer",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['pyck', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Code Analysis",
        "License :: OSI Approved :: BSD License",
    ],
    scripts=[
        'bin/pyck'
        ],
)
