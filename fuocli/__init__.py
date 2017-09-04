# -*- coding: utf-8 -*-

from .globals import _app_ctx


try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


def get_app_ctx():
    return _app_ctx