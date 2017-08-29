# -*- coding: utf-8 -*-

import logging
from functools import wraps

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


def call_cmd_handler(cmd, *args, **kwargs):
    if cmd not in list_commands():
        raise CommandNotFound('{}: command not found'.format(cmd))
    return _commands_to_handlers[cmd](*args, **kwargs)


@cmd('ls')
def ls():
    pass


@cmd('cd')
def cd():
    app_ctx = get_app_ctx()
    logger.debug(app_ctx.workspace)
