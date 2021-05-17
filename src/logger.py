import logging

from src import config


class Logger(logging.Logger):
    def __init__(self, name: str, level=config.logger.level) -> None:
        super().__init__(name, level=level)
        formatter = logging.Formatter(config.logger.format_)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(config.logger.level)
        self.addHandler(handler)
