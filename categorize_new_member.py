def categorize_new_member(data):
    return ["Senior" if d[0] >= 55 and d[1] > 7 else "Open" for d in data]

