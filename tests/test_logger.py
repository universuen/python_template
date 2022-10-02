import context

from src._logger import config, Logger

if __name__ == '__main__':
    config.config_name = 'test_logger'
    logger = Logger('test')
    logger.info('You should see me in both console and log file.')
