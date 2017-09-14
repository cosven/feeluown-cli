# -*- coding: utf-8 -*-

import logging
import time
from functools import wraps

logger = logging.getLogger(__name__)


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time.process_time()
        result = func(*args, **kwargs)
        elapsed_time = time.process_time() - t
        logger.info('function {} executed time: {:.6f} s'
                    .format(func.__name__, elapsed_time))
        return result
    return wrapper
