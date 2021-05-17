import logging


class ColorFormatter(logging.Formatter):
    def __init__(self, theme: dict, fmt=None, datefmt=None, style='%', validate=True):
        super().__init__(fmt, datefmt, style, validate)
        self.theme = theme

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        if record.levelname not in self.theme.keys():
            return message
        else:
            style_and_color = self.theme[record.levelname]
            return f"\033[{style_and_color[0]};{style_and_color[1]};{style_and_color[2]}m{message}\033[0;0m"
