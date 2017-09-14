# -*- coding: utf-8 -*-

import logging
from functools import wraps

from fuocli.exc import CommandAlreadyExists, CommandNotFound


__all__ = (
    'list_commands',
    'call_cmd_handler',
)

logger = logging.getLogger(__name__)

_commands = set()
_commands_to_handlers = {}
_commands_to_completers = {}


def list_commands():
    return list(_commands)


def register_cmd(name, handler, options=[], completer=None):
    _commands.add(name)
    _commands_to_handlers[name] = handler
    _commands_to_completers[name] = completer


def set_completer(name, completer):
    _commands_to_completers[name] = completer


def set_options(name, options):
    pass


def cmd(name, completer=None):
    if name in _commands:
        raise CommandAlreadyExists()

    _commands.add(name)
    _commands_to_completers[name] = completer

    def decorator(func):

        _commands_to_handlers[name] = func

        @wraps(func)
        def _wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return _wrapper

    return decorator


def option(name):

    def decorator(func):
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


def get_cmd_completer(name):
    return _commands_to_completers[name]
