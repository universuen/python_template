import logging

"""
For the purpose of reusing, relevant import is used here.
In actual project, absolute import is better.
"""
from .. import settings
from ._color_formatter import ColorFormatter


class Logger(logging.Logger):
    def __init__(self, name: str, file=settings.logger.file, level=settings.logger.level) -> None:
        super().__init__(name, level=level)

        # set formatter
        formatter = ColorFormatter(settings.logger.format_)

        # set handler
        if file:
            handler = logging.FileHandler(file)
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(settings.logger.level)
        self.addHandler(handler)
