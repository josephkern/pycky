#!/usr/bin/env python
"""Determines the dependencies of a python corpus using the internal
AST(Abstract Source Tree) reference.

This is much more accurate and less tiring than running:
`grep -R import *` on a source directory.

Usage:
  pyck file.py
  pyck [--all|-a] file.py 
  pyck [--help|-h] >> "this usage"

Written by Joseph Kern, 2011

TODO: Upload to github
TODO: Upload to pypi

TODO: Add flag for --no-search
TODO: Add try; except for internetaccess
TODO: Add pypi search (url to search result)
TODO: Add github search (url to search result)
TODO: Add google search (as a fall back "python package <modulename>)

"""

import os
import sys

import ast
import _ast

class Pyck(object):
    def __init__ (self,filename):
        self.filename = filename
        self.AST = None # AST Generator Placeholder
        self.ModuleNames = [ ]
        self.ImportTest = {True: [], False: []}

    def Parse(self):
        try:
            input_file = open(self.filename, 'r')
            python_file = input_file.read()

        except IOError:
            print("Problem opening the file {0} ...").format(filename)
            sys.exit(1)

        else:
            self.AST = ast.parse(python_file)

    def Filter(self,ast_object=_ast.Import):
        for element in ast.walk(self.AST):
            if element.__class__ == ast_object:
                for name in element.names:
                    self.ModuleNames.append(name.name)
                    # This currently will append the import element
                    # name as a str.

    def Test(self):
        """Tries to import modules (via exec()), returns a dictionary of
        values; k,v = {<module_name>: <boolean>}
        
        According to pydoc there are implicit *finders* for import"""

        while len(self.ModuleNames) > 0:
            module = self.ModuleNames.pop()
            try:
                exec "import " + module
                self.ImportTest[True].append(module)
            except ImportError:
                self.ImportTest[False].append(module)
    
    def Run(self):
        self.Parse()
        self.Filter()
        self.Test()

        return self.ImportTest
