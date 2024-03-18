import path_setup

from src.logger import Logger
from src.utils import get_script_name
from src.configs.common_configs import LoggerConfig

logger_config = LoggerConfig()
logger = Logger(get_script_name(), **logger_config)
logger.info('This is an info message.')

logger.set_level('ERROR')
logger.info("You shouldn't see me")
