from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(str(a) for a in args)
        kwargs_str = ", ".join(f"{str(k)}={str(v)}" for k, v in kwargs.items())
        all_args = ", ".join(x for x in [args_str, kwargs_str] if x)
        result = function(*args, **kwargs)
        return f"you called {function.__name__}({all_args})\nit returned {result}"
    return wrapper
