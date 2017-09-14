# -*- coding: utf-8 -*-

"""
    fuocli.app
    ~~~~~~~~~~

    ...
"""

import logging

from prompt_toolkit.completion import Completer, Completion


logger = logging.getLogger(__name__)


class DefaultCompleter(Completer):
    def get_completions(self, document, complete_event):
        from fuocli.cmd import list_commands, get_cmd_completer

        text = document.text
        parts = text.split(' ')

        # complete commands
        if len(parts) <= 1:
            for name in list_commands():
                if name.startswith(text):
                    yield Completion(name, start_position=-len(text))
        else:
            cmd_name = parts[0]
            if cmd_name in list_commands():
                completer = get_cmd_completer(cmd_name)
                for c in completer.get_completions(document, complete_event):
                    yield c
