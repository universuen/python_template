import context

from utils import gather_configs
import configs

def print_configs():
    for config in gather_configs():
        print(config)
    print()

if __name__ == '__main__':
    print_configs()

    class MyLoggerConfig(configs.LoggerConfig):
        level: int | str = 'DEBUG'
        new_attr: int = 1
    
    print_configs()

    configs.LoggerConfig.level = -100

    print_configs()

    print(configs.LoggerConfig().to_dict())

    from configs import LoggerConfig
    LoggerConfig.level = 'WARNING'

    print_configs()
