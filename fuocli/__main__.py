# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

from prompt_toolkit import prompt
from prompt_toolkit.styles import style_from_pygments
from pygments.styles.tango import TangoStyle
from pygments.lexers.sql import MySqlLexer

from fuocli import cmd, DefaultCompleter, DefaultLexer


logging.basicConfig(filename='fuocli.log', level=logging.DEBUG)


@cmd('play')
def play():
    pass


@cmd('create_playlist')
def create_playlist():
    pass


default_style = style_from_pygments(TangoStyle)


while True:
    text = prompt('> ', completer=DefaultCompleter(), lexer=MySqlLexer)
    print(text)
