def even_parameters(function):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, int) or value % 2 != 0:
                return "Please use only even numbers!"

        for value in kwargs.values():
            if not isinstance(value, int) or value % 2 != 0:
                return "Please use only even numbers!"

        return function(*args, **kwargs)
    return wrapper
