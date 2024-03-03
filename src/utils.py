from types import MethodType, FunctionType


def enable_grad(func: MethodType | FunctionType) -> MethodType | FunctionType:
    return func.__closure__[1].cell_contents
