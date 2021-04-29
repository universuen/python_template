from src.logger import Logger


if __name__ == '__main__':
    logger = Logger('test')
    logger.debug('why so serious')
    logger.info('wow')
    print('wow', end='')
    print({1: 2})
