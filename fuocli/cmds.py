# -*- coding: utf-8 -*-

import logging
from functools import wraps

from prompt_toolkit.shortcuts import clear

from fuocli import get_app_ctx
from fuocli.exc import CommandAlreadyExists, CommandNotFound


__all__ = (
    'list_commands',
    'call_cmd_handler',
)

logger = logging.getLogger(__name__)

_commands = set()
_commands_to_handlers = {}


def list_commands():
    return list(_commands)


def cmd(name):
    if name in _commands:
        raise CommandAlreadyExists()

    _commands.add(name)

    def decorator(func):

        _commands_to_handlers[name] = func

        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return _wrapper

    return decorator


def call_cmd_handler(result):
    if not result:
        return

    cmd, *args_str = result.split(' ', 1)
    args_str = args_str[0] if args_str else None

    if cmd not in list_commands():
        raise CommandNotFound('{}: command not found'.format(cmd))

    if args_str is not None:
        return _commands_to_handlers[cmd](args_str)
    else:
        return _commands_to_handlers[cmd]()


@cmd('cd')
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
