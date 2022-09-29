from __future__ import annotations
from pathlib import Path
import logging


class Paths:
    src: Path = Path(__file__).absolute().parent
    project: Path = src.parent
    data: Path = project / 'data'
    scripts: Path = project / 'scripts'
    tests: Path = project / 'tests'
    logs: Path = project / 'logs'


# create path if not exists
for i in list(vars(Paths).values()):
    if isinstance(i, Path):
        i.mkdir(parents=True, exist_ok=True)


class Logger:
    message_fmt: str = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
    level: int = logging.DEBUG
    date_fmt: str = '%Y-%m-%d %H:%M:%S'
    log_path: Path | str = Paths.logs
