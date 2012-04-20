#!/usr/bin/python
"""Determines the dependencies of a python corpus using the internal
AST(Abstract Source Tree) reference.

This is much more accurate and less tiring than running:
`grep -R import *` on a source directory.

Usage:
  pyck file.py
  pyck [--all|-a] file.py 
  pyck [--help|-h] >> "this usage"

Written by Joseph Kern, 2011

TODO: Make a proper package (as a python executable)
TODO: Refactor based on best practices etc.
TODO: Upload to github
TODO: Upload to pypi
TODO: Make a landing page on code.semafour.net/pyck

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


def getAST(filename):
    """Arguments: filename: path to the file to be checked.
    Returns an ast generator of the supplied file."""

    try:
        infile = open(filename, 'r')
        python_file = infile.read()

    except IOError:
        print("Problem opening the file {0} ...").format(filename)

    else:
        return ast.parse(python_file)

def filterAST(ast_generator, ast_object=_ast.Import):
    """Expects a generator or sequence of _ast objects. Will return a
    list of all objects of the class defined with ast_object"""

    objects = [ ]
    for element in ast.walk(ast_generator):
        if element.__class__ == ast_object:
            objects.append(element)
    return objects

def getModuleNames(objects):
    """Finds the names of _ast.Import objects."""

    module_list = [ ]
    for element in objects:
        for name in element.names:
            module_list.append(name.name)
    return module_list

def testImport(module_list):
    """Tries to import modules (via exec()), returns a dictionary of
    values; k,v = {<module_name>: <boolean>}

    According to pydoc there are implicit *finders* for import"""

    module_check = {}
    # This would be better served as {True: [], False: []}
    for module in module_list:
        if not module_check[module]:
            try:
                exec "import " + module
                module_check[module] = true
            except ImportError:
                module_check[module] = false
        else:
            continue
    return module_check

# Clean this up, it's getting to the point where an object would be
# easier.  Each object could be responsible for a single python AST
# (organized by file), all objects returning a dictionary like: 
# {True: [], False: []}

def main():
    data = getAST(sys.argv[1])
    imports = filterAST(data)
    print("\n".join(getModuleNames(imports)))
    #testImport

if __name__ == "__main__":
    main()
