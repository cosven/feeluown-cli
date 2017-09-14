# -*- coding: utf-8 -*-


class FuocliException(Exception):
    pass


class CommandAlreadyExists(FuocliException):
    pass


class CommandNotFound(FuocliException):
    pass


class VfsError(FuocliException):
    pass


class NoSuchDir(VfsError):
    pass
