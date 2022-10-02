from __future__ import annotations
from pathlib import Path
import logging

from src._config import Config


class Paths(Config):
    src: Path = Path(__file__).absolute().parent
    project: Path = src.parent
    data: Path = project / 'data'
    scripts: Path = project / 'scripts'
    tests: Path = project / 'tests'
    logs: Path = data / 'logs'


# create path if not exists
for i in list(vars(Paths).values()):
    if isinstance(i, Path):
        i.mkdir(parents=True, exist_ok=True)


class Logger(Config):
    message_fmt: str = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
    level: int = logging.DEBUG
    date_fmt: str = '%Y-%m-%d %H:%M:%S'
    logs_path: Path = Paths.logs
