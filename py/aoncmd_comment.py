"""create a comment on a differential review."""

import argparse
import sys
import textwrap

import phlcon_differential
import phlsys_makeconduit


def getFromfilePrefixChars():
    return ""


def setupParser(parser):
    actions = parser.add_argument_group(
        'action argument',
        'use any of ' + textwrap.fill(
            str(phlcon_differential.USER_ACTIONS.keys())))

    parser.add_argument(
        'ids',
        type=int,
        nargs="*",
        default=[],
        help="the revision to comment on (e.g. 1)")
    parser.add_argument(
        '--ids-file',
        metavar='FILE',
        type=argparse.FileType('r'),
        help="a file to read ids from, use '-' to specify stdin")

    parser.add_argument(
        '--message', '-m',
        metavar="M",
        default="",
        type=str,
        help="the body text of the comment")
    parser.add_argument(
        '--message-file',
        metavar='FILE',
        type=argparse.FileType('r'),
        help="a file to read the message from, use '-' for stdin")
    parser.add_argument(
        '--silent',
        action='store_true',
        help="don't send notification emails for this comment")

    actions.add_argument(
        '--action', '-a',
        choices=phlcon_differential.USER_ACTIONS.keys(),
        metavar="ACTION",
        default='comment',
        type=str,
        help="perform an action on a review")


def process(args):
    conduit = phlsys_makeconduit.makeConduit()

    d = {
        'message': args.message,
        'silent': args.silent,
        'action': phlcon_differential.USER_ACTIONS[args.action]
    }

    if args.message_file:
        d['message'] += args.message_file.read()

    ids = args.ids
    if args.ids_file:
        ids.extend([int(i) for i in args.ids_file.read().split()])

    if not ids:
        print "error: you have not specified any revision ids"
        sys.exit(1)

    for i in ids:
        d["revision_id"] = i
        result = conduit.call("differential.createcomment", d)
        print result


#------------------------------------------------------------------------------
# Copyright (C) 2012 Bloomberg L.P.
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
#------------------------------- END-OF-FILE ----------------------------------