def squares(limit):
    limit = limit + 1
    n = 1
    while n < limit:
        yield n * n
        n += 1
