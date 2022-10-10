from __future__ import annotations

import logging
from pathlib import Path

"""
Attention: To guarantee the code's low-coupling and reusability, 
please do not import this module in any `src` modules except `api`.
"""


class _Config:
    @classmethod
    def to_dict(cls) -> dict:
        result = dict()
        for k, v in vars(cls).items():
            if k.startswith('_') or k in ('i', 'j', 'k'):
                continue
            result[k] = v
        return result

    @classmethod
    def print_content(cls):
        print(cls.__name__)
        for k, v in cls.to_dict().items():
            print(f'\t{k}: {v}')


class Paths(_Config):
    src: Path = Path(__file__).absolute().parent
    project: Path = src.parent
    data: Path = project / 'data'
    scripts: Path = project / 'scripts'
    tests: Path = project / 'tests'
    logs: Path = data / 'logs'

    # create path if not exists
    for i in list(vars().values()):
        if isinstance(i, Path):
            i.mkdir(parents=True, exist_ok=True)


class Logger(_Config):
    level = logging.INFO
