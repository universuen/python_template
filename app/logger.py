"""
Using loggers in your project helps you develop more efficiently.
"""

import logging

from . import config


class Logger(logging.Logger):
    def __init__(self, name: str, level=config.logger.level) -> None:
        super().__init__(name, level=level)
        formatter = logging.Formatter(
            fmt=config.logger.fmt,
            datefmt=config.logger.datefmt,
        )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(config.logger.level)
        self.addHandler(handler)
