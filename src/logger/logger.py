import logging

from src import config


class ColoredFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', validate=True):
        super().__init__(fmt, datefmt, style, validate)

    def format(self, record: logging.LogRecord) -> str:
        if record.levelname not in config.logger.style_and_color.keys():
            return super().format(record)
        style_and_color = config.logger.style_and_color[record.levelname]
        for i in style_and_color.keys():
            try:
                setattr(record, i, f"\033[{style_and_color[i][0]};"
                                   f"{style_and_color[i][1]};"
                                   f"{style_and_color[i][2]}m"
                                   f"{getattr(record, i)}"
                                   f"\033[0;0m")
            except AttributeError:
                pass

        return super().format(record)


class Logger(logging.Logger):
    def __init__(self, name: str, file=config.logger.file, level=config.logger.level) -> None:
        super().__init__(name, level=level)

        # set formatter
        formatter = ColoredFormatter(config.logger.format_)

        # set handler
        if file:
            handler = logging.FileHandler(file)
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(config.logger.level)
        self.addHandler(handler)
