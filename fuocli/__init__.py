# -*- coding: utf-8 -*-

from functools import wraps
import logging

from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.layout.lexers import Lexer
from prompt_toolkit.token import Token

from .exc import CommandAlreadyExists


__all__ = (
    'list_commands',
    'call_cmd_handler'
)

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

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


def call_cmd_handler(cmd, *args):
    return cmd(args)


class DefaultCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text
        for name in list_commands():
            if name.startswith(text):
                yield Completion(name, start_position=-len(text))


class DefaultLexer(Lexer):
    def lex_document(self, cli, document):

        lines = document.lines

        def get_line(lineno):
            " Return the tokens for the given line. "
            try:
                line = lines[lineno]
                if ' ' not in line:
                    return [(Token, lines[lineno])]

                command = line.split(' ')[0]
                text = line.split(' ')[1]
                return [(Token.Keyword, command),
                        (Token.Whitespace, ' '),
                        (Token.Text, text)]
            except IndexError:
                import pdb
                pdb.set_trace()

        return get_line
