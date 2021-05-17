import logging

from src.logger import Logger as BasicLogger
from src.logger.theme import Style, TextColor, BackgroundColor

file = None
format_ = '%(name)-10s: %(levelname)-10s: %(message)-100s'
level = logging.DEBUG

theme = {
    'DEBUG': [Style.bold, TextColor.black, BackgroundColor.cyan],
    'INFO': [Style.bold, TextColor.black, BackgroundColor.yellow],
    'WARNING': [Style.bold, TextColor.black, BackgroundColor.purple],
    'ERROR': [Style.bold, TextColor.black, BackgroundColor.red],
}


class Logger(BasicLogger):
    def __init__(self, name: str):
        super().__init__(name, theme=theme, format_=format_, level=level, file=file)
