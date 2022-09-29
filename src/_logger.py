"""
Using loggers in your project helps you develop more efficiently.
"""

import logging
import sys
import os

from src import config


class Logger(logging.Logger):
    def __init__(self, name: str, level=config.Logger.level) -> None:
        super().__init__(name, level=level)
        formatter = logging.Formatter(
            fmt=config.Logger.message_fmt,
            datefmt=config.Logger.date_fmt,
        )
        s_handler = logging.StreamHandler(stream=sys.stdout)
        s_handler.setFormatter(formatter)
        s_handler.setLevel(config.Logger.level)
        f_handler = logging.FileHandler(os.path.join(config.Logger.log_path, f'{name}.log'))
        f_handler.setFormatter(formatter)
        f_handler.setLevel(config.Logger.level)
        self.addHandler(s_handler)
        self.addHandler(f_handler)
