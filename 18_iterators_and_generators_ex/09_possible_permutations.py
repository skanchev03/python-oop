def possible_permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            first = lst[i]
            rest = lst[:i] + lst[i+1:]
            for perm in possible_permutations(rest):
                yield [first] + perm
