from __future__ import annotations

from typing import Type
import logging
from pathlib import Path

"""
Attention: To guarantee the code's low-coupling and reusability, 
please do not import this module in any `src` modules except `api`.
"""

# registry = dict()

# def _get_pure_vars(obj):
#     result = dict()
#     for k, v in vars(obj).items():
#         if k[0] == '_':
#             continue
#         if k in registry.keys():
#             result[k] = registry[k]
#             del registry[k]
#         else:
#             result[k] = v
#     return result

# def _registered_config(ConfigClass):
#     registry[ConfigClass.__name__] = _get_pure_vars(ConfigClass)
#     return ConfigClass



class _Config:
    @classmethod
    def to_dict(cls) -> dict:
        result = dict()
        for k, v in vars(cls).items():
            if k.startswith('_') or k in ('i', 'j', 'k'):
                continue
            result[k] = v
        return result


ConfigType = Type[_Config]


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


_all_items = vars().values()


def get_all_configs() -> list[ConfigType]:
    results = []
    for i in _all_items:
        try:
            if issubclass(i, _Config) and not i.__name__.startswith('_'):
                results.append(i)
        except TypeError:
            pass
    return results
