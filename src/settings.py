import pathlib
import logging


class Path:
    src = pathlib.Path(__file__).absolute().parent
    project = src.parent


class Logger:
    format = '[%(name)-10s] %(levelname)-8s: %(message)s'
    level = logging.DEBUG
