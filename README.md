Determines the dependencies of python source files using the internal python
AST(Abstract Source Tree) rather than regular expressions.

This is much more accurate and less tiring than running:
`grep -R import *` on a source directory.


Usage
----------

    pycky <python file(s)>
    _ast 		: Installed
    ast 		: Installed
    sys 		: Installed
    test		: Missing


Installation
----------

	python setup.py install



