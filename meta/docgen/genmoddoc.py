""""Automatically generate documentation from module docstrings."""
# =============================================================================
# CONTENTS
# -----------------------------------------------------------------------------
# genmoddoc
#
# Public Functions:
#   main
#
# -----------------------------------------------------------------------------
# (this contents block is generated, edits will be lost)
# =============================================================================

from __future__ import print_function

import argparse
import ast
import os
import sys


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        'modules',
        type=str,
        nargs="+")
    argparser.add_argument(
        '--docfile',
        type=argparse.FileType('w'),
        required=True)
    args = argparser.parse_args()

    modules = sorted(args.modules)
    for m in modules:
        module = ast.parse(''.join(open(m)))
        doc = ast.get_docstring(module)

        if doc:
            print('* `' + os.path.basename(m) + '` -', file=args.docfile)
            print(doc.splitlines()[0], file=args.docfile)
        else:
            print('* `' + os.path.basename(m) + '`', file=args.docfile)


if __name__ == "__main__":
    sys.exit(main())

# -----------------------------------------------------------------------------
# Copyright (C) 2013-2014 Bloomberg Finance L.P.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ------------------------------ END-OF-FILE ----------------------------------
