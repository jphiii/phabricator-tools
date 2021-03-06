"""Wrapper around 'git push'."""
# =============================================================================
# CONTENTS
# -----------------------------------------------------------------------------
# phlgit_push
#
# Public Functions:
#   push_asymmetrical_force
#   push_asymmetrical
#   push
#   force_branch
#   branch
#   move_asymmetrical
#   delete
#
# -----------------------------------------------------------------------------
# (this contents block is generated, edits will be lost)
# =============================================================================

from __future__ import absolute_import

import itertools


def push_asymmetrical_force(repo, localBranch, remoteBranch, remoteName):
    repo('push', remoteName, localBranch + ":" + remoteBranch, "--force")


def push_asymmetrical(repo, localBranch, remoteBranch, remoteName):
    repo('push', remoteName, localBranch + ":" + remoteBranch)


def push(repo, branch, remoteName):
    repo('push', remoteName, branch)


def force_branch(repo, branch, remote='origin'):
    """Force push 'branch' to the supplied 'origin'.

    :repo: a callable supporting git commands, e.g. repo("status")
    :branch: the string name of the branch to push
    :remote: the string name of the remote to push to
    :returns: None

    """
    repo('push', '--force', remote, branch)


def branch(repo, branch, remote='origin'):
    repo('push', remote, branch)


def move_asymmetrical(repo, local_branch, old_remote, new_remote, remote):
    """Delete 'old_remote', push 'local_branch' to 'new_remote' on 'remote'.

    :repo: a callable supporting git commands, e.g. repo("status")
    :local_branch: the local reference to push
    :old_remote: the old reference on the remote to delete
    :new_remote: the new reference on the remote to push to
    :remote: the name of the remote to push to
    :returns: None

    """
    repo(
        'push',
        remote,
        local_branch + ":" + new_remote,
        ":" + old_remote)


def delete(repo, remote, branch, *args):
    """Delete 'branch' from the specified remote.

    :repo: a callable supporting git commands, e.g. repo("status")
    :remote: string name of the remote
    :branch: string name of the branch
    :*args: (optional) more string names of branches
    :returns: None

    """
    removals = [':' + b for b in itertools.chain([branch], args)]
    repo('push', remote, *removals)

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
