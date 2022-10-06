import src
from src import config


def get_configured_logger(name: str):
    return src.logger.Logger(
        name=name,
        level=src.config.Logger.level,
        logs_dir=src.config.Paths.logs,
    )
