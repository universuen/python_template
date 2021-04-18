import logging
import settings


class Logger(logging.Logger):
    def __init__(self, name: str, level=settings.Logger.level) -> None:
        super().__init__(name, level=level)
        formatter = logging.Formatter(settings.Logger.format)
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(settings.Logger.level)
        self.addHandler(handler)
