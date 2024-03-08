import context

from src.logger import Logger


logger = Logger('test', 'INFO')
logger.info('This is an info message.')

logger.set_level('ERROR')
logger.info("You shouldn't see me")
