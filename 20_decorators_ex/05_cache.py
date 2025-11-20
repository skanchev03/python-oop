def cache(function):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]

        result = function(n)
        log[n] = result
        return result

    wrapper.log = log
    return wrapper
