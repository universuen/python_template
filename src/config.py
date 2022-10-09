from __future__ import annotations

import logging
from pathlib import Path

"""
Attention: To guarantee the code's low-coupling and reusability, 
please do not import this module in any `src` modules except `api`.
"""


class _Config:
    def to_dict(self) -> dict:
        result = dict()
        for k, v in vars(self.__class__).items():
            if k.startswith('_'):
                continue
            if type(v) is property:
                v = getattr(self, k)
            result[k] = v
        return result

    def __repr__(self):
        result = f'<{self.__class__.__name__[1:]}Config> (\n'
        for k, v in self.to_dict().items():
            result += f'\t{k}: {v}\n'
        result += ')'
        return result


class _Path(_Config):
    src: Path = Path(__file__).absolute().parent
    project: Path = src.parent
    data: Path = project / 'data'
    scripts: Path = project / 'scripts'
    tests: Path = project / 'tests'
    logs: Path = data / 'logs'

    # create path if not exists
    def __init__(self):
        for i in list(self.to_dict().values()):
            i.mkdir(parents=True, exist_ok=True)


path = _Path()


class _Logger(_Config):
    level: int | str = logging.INFO

    @property
    def logs_dir(self) -> Path:
        return path.logs


logger = _Logger()
