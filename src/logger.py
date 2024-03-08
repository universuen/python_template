import logging
import sys
from pathlib import Path


class Logger(logging.Logger):
    def __init__(
            self,
            name: str,
            level: int | str = logging.INFO,
            logs_dir: Path = None,
    ) -> None:
        super().__init__(name, level=level)

        formatter = logging.Formatter(
            fmt='%(asctime)s [%(name)s] [%(levelname)s]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

        s_handler = logging.StreamHandler(stream=sys.stdout)
        s_handler.setFormatter(formatter)
        s_handler.setLevel(level)
        self.addHandler(s_handler)

        if logs_dir is not None:
            logs_dir.mkdir(exist_ok=True)
            log_file = logs_dir / f'{name}.log'
            f_handler = logging.FileHandler(log_file, 'a')
            f_handler.setFormatter(formatter)
            f_handler.setLevel(level)
            self.addHandler(f_handler)

    def set_level(self, level: int | str) -> None:
        self.setLevel(level)
        for handler in self.handlers:
            handler.setLevel(level)
