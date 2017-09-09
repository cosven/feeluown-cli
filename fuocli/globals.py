# -*- coding: utf-8 -*-

"""
    fuocli.globals
    ~~~~~~~~~~~~~~

    ...
"""

from fuocore import source

from .ctx import AppContext
from .vfs import FuoVfs

_app_ctx_stack = None
_fuo_vfs = FuoVfs(source)
_app_ctx = AppContext(_fuo_vfs, _fuo_vfs.root)
