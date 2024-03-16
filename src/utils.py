import inspect
from types import MethodType, FunctionType
from pathlib import Path

import torch
import random
import numpy as np


def enable_grad_for_hf_llm(func: MethodType | FunctionType) -> MethodType | FunctionType:
    return func.__closure__[1].cell_contents


def get_script_name() -> str:
    caller_frame_record = inspect.stack()[1]
    module_path = caller_frame_record.filename
    return Path(module_path).stem


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
