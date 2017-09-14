# -*- coding: utf-8 -*-

import logging
import os

from prompt_toolkit.completion import Completion
from prompt_toolkit.shortcuts import clear

from fuocli import get_app_ctx
from fuocli.cmd import cmd
from fuocli.utils import measure_time
from fuocli.vfs import isdir


logger = logging.getLogger(__name__)


class BaseCmdComplter(object):
    """
    One cmd completer consists of two parts: options completer
    and values completer.

    tree structure::

                     --------  cmd(name)  -------
                  /                |               \
              options            args(1)           args(2)
            /  |  |  \         /    |   \             |
          -a  -c  -l -z      abc   bfs  meme         ...
         /
        1
    """
    pass


class ChdirCompleter(BaseCmdComplter):

    @measure_time
    def get_completions(self, document, complete_event):
        app_ctx = get_app_ctx()
        curdir = app_ctx.curdir

        text = document.text
        parts = text.split(' ', 1)
        path = os.path.normpath(parts[1]) if parts[1] else ''
        logger.debug('{}: path to complete'.format(path))

        # get dirname and basename
        dirname = os.path.dirname(path)
        basename = os.path.basename(path)
        if not dirname:
            dir_abspath = curdir.path
        else:
            dir_abspath = dirname
        logger.debug('{}: absolute directory path '.format(dir_abspath))
        entry = app_ctx.vfs.path_lookup(dir_abspath)
        if entry is None:
            return []
        if isdir(entry):
            for each in entry:
                yield Completion(each.name, start_position=-len(basename))


@cmd('cd', completer=ChdirCompleter())
def cd(path=None):
    logger.debug('prepare to chdir to: {}'.format(path))
    app_ctx = get_app_ctx()
    if path is not None:
        app_ctx.chdir(path)
        logger.debug(app_ctx.getcwd())


@cmd('clear')
def clear_():
    clear()


@cmd('exit')
def exit():
    raise EOFError


@cmd('ls')
def ls():
    app_ctx = get_app_ctx()
    vfs = app_ctx.vfs
    for f in vfs.listdir(app_ctx.curdir):
        print(f)


@cmd('pwd')
def pwd():
    app_ctx = get_app_ctx()
    print(app_ctx.getcwd())
