import torch

from dataclasses import dataclass, asdict
from pathlib import Path
import logging


def config_class(cls):
    cls = dataclass(cls)

    def to_dict(self) -> dict:
        return asdict(self)

    setattr(cls, "to_dict", to_dict)
    return cls


@config_class
class PathConfig:
    project: Path = Path(__file__).absolute().parent
    src: Path = project / 'src'
    data: Path = project / 'data'
    scripts: Path = project / 'scripts'
    tests: Path = project / 'tests'
    logs: Path = data / 'logs'

    def __post_init__(self) -> None:
        for path in vars(self).values():
            path.mkdir(parents=True, exist_ok=True)


@config_class
class LoggerConfig:
    level: int | str = logging.INFO
    logs_dir: Path = PathConfig().logs


@config_class
class OtherConfig:
    device: str = 'default'

    def __post_init__(self) -> None:
        if self.device == 'default':
            if torch.cuda.is_available():
                self.device = 'cuda'
            else:
                self.device = 'cpu'
