#!/usr/bin/env python
"""
Written by Joseph Kern, 2011
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
