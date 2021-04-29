from src.logger import Logger


if __name__ == '__main__':
    logger = Logger('test')
    logger.debug('why so serious')
    logger.info('why so serious')
    logger.warning('why so serious')
    logger.error('why so serious')
