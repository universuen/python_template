import context

import src


if __name__ == '__main__':
    logger = src.api.get_configured_logger('test')
    logger.debug('test_debug')
    logger.info('test_info')
