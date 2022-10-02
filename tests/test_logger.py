import context

from src.logger import config, Logger

if __name__ == '__main__':
    logger = Logger('test')
    logger.info('You should see me in both console and log file.')
