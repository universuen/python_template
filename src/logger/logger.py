import logging
from typing import Union

from src.logger._color_formatter import ColorFormatter
from src.logger.theme import Style, TextColor, BackgroundColor


class Logger(logging.Logger):
    def __init__(
            self,
            name: str,
            theme: dict = None,
            format_: str = None,
            level: Union[str, int] = 'INFO',
            file: str = None
    ) -> None:
        super().__init__(name, level=level)
        if theme is None:
            theme = {
                'DEBUG': [Style.default, TextColor.default, BackgroundColor.default],
                'INFO': [Style.default, TextColor.default, BackgroundColor.default],
                'WARNING': [Style.default, TextColor.default, BackgroundColor.default],
                'ERROR': [Style.default, TextColor.default, BackgroundColor.default],
            }
        # set formatter
        formatter = ColorFormatter(theme, format_)

        # set handler
        if file:
            handler = logging.FileHandler(file)
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(level)
        self.addHandler(handler)
