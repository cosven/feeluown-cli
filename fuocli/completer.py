# -*- coding: utf-8 -*-

"""
    fuocli.app
    ~~~~~~~~~~

    ...
"""


from prompt_toolkit.completion import Completer, Completion

from fuocli.cmds import list_commands


class DefaultCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text
        for name in list_commands():
            if name.startswith(text):
                yield Completion(name, start_position=-len(text))
