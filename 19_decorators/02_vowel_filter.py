def vowel_filter(function):
    def wrapper():
        return [letter for letter in function() if letter in 'aeiou']

    return wrapper
