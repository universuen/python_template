"""
Using loggers in your project helps you develop more efficiently.
"""
from __future__ import annotations

import logging
import sys
import os
from pathlib import Path
from warnings import warn

from src import config


class Logger(logging.Logger):
    def __init__(
            self,
            name: str,
            level: int | str = config.Logger.level,
            log_dir: Path = None,
    ) -> None:
        super().__init__(name, level=level)
        formatter = logging.Formatter(
            fmt=config.Logger.message_fmt,
            datefmt=config.Logger.date_fmt,
        )

        s_handler = logging.StreamHandler(stream=sys.stdout)
        s_handler.setFormatter(formatter)
        s_handler.setLevel(config.Logger.level)

        log_dir = config.Logger.logs_path / config.config_name if log_dir is None else log_dir
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / f'{name}.log'
        if os.path.exists(log_file):
            warn(f'{log_file} already exists!')
        f_handler = logging.FileHandler(log_file)
        f_handler.setFormatter(formatter)
        f_handler.setLevel(config.Logger.level)

        self.addHandler(s_handler)
        self.addHandler(f_handler)
