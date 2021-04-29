import logging

from src.config.logger.style_and_color import Style, TextColor, BackgroundColor


file = None
format_ = '%(name)-10s%(levelname)-8s: %(message)s'
level = logging.DEBUG

style_and_color = {
    'DEBUG': {
        # 'name': [Style.bold, TextColor.white, BackgroundColor.yellow],
        'levelname': [Style.normal, TextColor.white, BackgroundColor.cyan],
    },
    'INFO': {
        'levelname': [Style.normal, TextColor.white, BackgroundColor.yellow],
    }
}