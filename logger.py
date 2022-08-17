#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Lonely_Dark---
# Python 3.10.5


import logging
import coloredlogs

log_format: str = '[%(asctime)s] [%(filename)s] [%(levelname)s] [%(lineno)d]: %(' \
         'message)s '

formatter = logging.Formatter(log_format)
formatter_color = coloredlogs.ColoredFormatter(log_format)

log_level = logging.DEBUG


def file_handler(filename: str) -> logging.FileHandler:
    """
    Adds a file handler to main logger
    :param filename: String, file to write
    :return: logging.FileHandler
    """
    handler: logging.FileHandler = logging.FileHandler(filename)
    handler.setLevel(log_level)
    handler.setFormatter(formatter)

    return handler


def stream_handler() -> logging.StreamHandler:
    """
    Adds a stream handler to main logger and log is colourful.
    :return: logging.StreamHandler
    """
    handler: logging.StreamHandler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(formatter_color)

    return handler


def get_logger(name: str, turn_file_handler: bool = False, filename: str = "avito.log") -> logging.Logger:
    """
    Gets the __name__ logger
    :param name: String, logger __name__
    :param turn_file_handler: Boolean, turn on file handler?
    :param filename: String, if turn_file_handler is True. Check filename
    :return: logging.Logger
    """
    logger: logging.Logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(stream_handler())

    if turn_file_handler is True:
        logger.addHandler(file_handler(filename))

    return logger
