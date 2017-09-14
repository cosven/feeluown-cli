# -*- coding: utf-8 -*-

"""
    fuocli.app
    ~~~~~~~~~~

    ...
"""

from prompt_toolkit import prompt_async, AbortAction

from fuocli.cmd import call_cmd_handler
from fuocli.cmds import *  # noqa, make commands available
from fuocli.completer import DefaultCompleter
from fuocli.exc import CommandNotFound
from fuocli.lexer import DefaultLexer


class App(object):

    def __init__(self):
        pass

    async def run(self):
        while True:
            try:
                result = await prompt_async(
                    '> ',
                    completer=DefaultCompleter(),
                    lexer=DefaultLexer,
                    on_abort=AbortAction.RETRY,
                    patch_stdout=True
                )
                call_cmd_handler(result)
            except EOFError:
                print('Goodbye')
                break
            except CommandNotFound as e:
                print(str(e))
