# -*- coding: utf-8 -*-

"""
    fuocli.app
    ~~~~~~~~~~

    ...
"""

from prompt_toolkit import prompt_async

from fuocli.cmds import call_cmd_handler
from fuocli.completer import DefaultCompleter
from fuocli.lexer import DefaultLexer


class App(object):

    def __init__(self):
        pass

    async def run(self):
        while True:
            result = await prompt_async('> ',
                                        completer=DefaultCompleter(),
                                        lexer=DefaultLexer)
            call_cmd_handler(result)
