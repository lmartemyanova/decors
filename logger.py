import datetime
import os
from functools import wraps


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        func_info = {
            'time': datetime.datetime.now(),
            'func_name': old_function.__name__,
            'args': f"""{
            args if args else "нет позиционных аргументов", 
            kwargs if kwargs else "нет именованных аргументов"
            }""",
            'return': old_function(*args, **kwargs)
        }
        with open(f'{os.getcwd()}/main.log', 'a', encoding='utf-8') as f:
            for key, value in func_info.items():
                f.write(f'{key}: {value} \n')
            f.write('\n')
        result = old_function(*args, **kwargs)
        return result
    return new_function
