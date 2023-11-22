import src
import configs


def gather_configs() -> list[configs.ConfigBase]:

    def recursively_get_sub_classes(cls: type) -> list[type]:
        all_sub_classes = []
        for subclass in cls.__subclasses__():
            all_sub_classes.append(subclass)
            all_sub_classes.extend(recursively_get_sub_classes(subclass))
        return all_sub_classes

    return [config() for config in recursively_get_sub_classes(configs.ConfigBase)]


def get_logger(name: str) -> src.Logger:
    return src.Logger(
        name, 
        level=configs.LoggerConfig().level, 
        logs_dir=configs.LoggerConfig().path,
    )
