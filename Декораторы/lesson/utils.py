import time
from datetime import datetime
from functools import wraps


def time_check(old_func):
    @wraps(old_func)
    def new_func(*args, **kwargs):
        start = datetime.now()
        result = old_func(*args, **kwargs)
        end = datetime.now()
        print(f'Функция {old_func} работала {end - start} секунд')
        return result
    return new_func


def attempts(old_func):
    @wraps(old_func)
    def new_func(*args, **kwargs):
        err = None
        for i in range(5):
            try:
                result = old_func(*args, **kwargs)
                return result
            except Exception as e:
                print(f'Попытка номер {i + 1} вызвать функцию {old_func} была неудачной')
                time.sleep(3)
                err = e
        raise err
    return new_func


def attempts2(count, delay):
    def decorator(old_func):
        @wraps(old_func)
        def new_func(*args, **kwargs):
            err = None
            for i in range(count):
                try:
                    result = old_func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f'Попытка номер {i + 1} вызвать функцию {old_func} была неудачной')
                    time.sleep(delay)
                    err = e
            raise err
        return new_func
    return decorator