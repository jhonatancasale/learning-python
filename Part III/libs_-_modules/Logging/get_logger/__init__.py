# -*- coding: utf-8 -*-

import logging


def get_logger(name: str, log_file: str, level=logging.DEBUG,
               formatter=logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
               ):
    """Configure and get a new logger"""

    handler = logging.FileHandler(log_file)
    handler.setLevel(level)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
