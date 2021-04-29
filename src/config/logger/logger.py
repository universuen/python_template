import logging

from src.config.logger.theme import Style, TextColor, BackgroundColor


file = None
format_ = '%(name)-10s: %(levelname)-10s: %(message)-100s'
level = logging.DEBUG

theme = {
    'DEBUG': [Style.bold, TextColor.black, BackgroundColor.cyan],
    'INFO': [Style.bold, TextColor.black, BackgroundColor.green],
    'WARNING': [Style.bold, TextColor.black, BackgroundColor.yellow],
    'ERROR': [Style.bold, TextColor.black, BackgroundColor.red],
}
