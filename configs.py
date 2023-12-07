from __future__ import annotations
from pathlib import Path
import logging


class Config:
    def __init__(self) -> None:
        for k, v in vars(self.__class__).items():
            if not k.startswith('__'):
                setattr(self, k, v)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        suffix = f"({', '.join(f'{key}={value}' for key, value in vars(self).items())})"
        return f'{class_name}{suffix}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def to_dict(self) -> dict[str, any]:
        return vars(self)


class PathConfig(Config):
    project: Path = Path(__file__).absolute().parent
    src: Path = project / 'src'
    data: Path = project / 'data'
    scripts: Path = project / 'scripts'
    tests: Path = project / 'tests'
    logs: Path = data / 'logs'

    def __init__(self) -> None:
        super().__init__()
        for path in vars(self).values():
            path.mkdir(parents=True, exist_ok=True)


class LoggerConfig(Config):
    level: int | str = logging.INFO
    path: Path = PathConfig().logs

