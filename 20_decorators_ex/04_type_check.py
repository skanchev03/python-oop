def type_check(some_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if not isinstance(args[0], some_type):
                return "Bad Type"
            return function(*args, **kwargs)
        return wrapper
    return decorator
