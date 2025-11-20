def tags(html_tag):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return f"<{html_tag}>{result}</{html_tag}>"
        return wrapper
    return decorator
