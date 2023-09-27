import context

import src
import configs


if __name__ == '__main__':
    logger = src.Logger(
        'test', 
        level=configs.LoggerConfig().level, 
        logs_dir=configs.LoggerConfig().path
    )
    logger.debug('test_debug')
    logger.info('test_info')
