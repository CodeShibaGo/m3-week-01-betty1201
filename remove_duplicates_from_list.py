def distinct(seq):
    unique_items = list(set(seq))
    result = []
    for i in seq:
        if i in unique_items:
            result.append(i)
            unique_items.remove(i)
    return result

def distinct(seq):
    return sorted(set(seq),key=seq.index)
