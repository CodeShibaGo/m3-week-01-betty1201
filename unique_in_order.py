def unique_in_order(iterable):
    result = []
    for i in iterable:
        if result == [] or result[-1] != i:
            result.append(i)
    return result