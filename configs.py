import torch

from dataclasses import dataclass
from pathlib import Path
import logging


@dataclass
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


@dataclass
class LoggerConfig:
    level: int | str = logging.INFO
    path: Path = PathConfig().logs


@dataclass
class OtherConfig:
    device: str = 'default'

    def __post_init__(self) -> None:
        if self.device == 'default':
            if torch.cuda.is_available():
                self.device = 'cuda'
            else:
                self.device = 'cpu'  
