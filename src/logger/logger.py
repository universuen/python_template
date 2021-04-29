import logging

from src import config
from src.logger._color_formatter import ColorFormatter


class Logger(logging.Logger):
    def __init__(self, name: str, file=config.logger.file, level=config.logger.level) -> None:
        super().__init__(name, level=level)

        # set formatter
        formatter = ColorFormatter(config.logger.format_)

        # set handler
        if file:
            handler = logging.FileHandler(file)
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(config.logger.level)
        self.addHandler(handler)
