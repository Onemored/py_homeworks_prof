from functools import wraps


def decorator(old_func):
    @wraps(old_func)
    def new_func(*args, **kwargs):
        # Код до вызова старой функции
        result = old_func(*args, **kwargs)
        # Код после вызова старой функции
        return result
    return new_func


def decorator_with_params(params):
    def decorator(old_func):
        @wraps(old_func)
        def new_func(*args, **kwargs):
            # Код до вызова старой функции. Можно применять params
            result = old_func(*args, **kwargs)
            # Код после вызова старой функции. Можно применять params
            return result
        return new_func
    return decorator

