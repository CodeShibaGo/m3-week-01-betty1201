def count_duplicates(text):
    dict = {}
    for i in text.lower():
        dict[i] = dict.get(i, 0) + 1

    ans = 0
    for i in dict.values():
        if i > 1:
            ans += 1
    return ans

# print(count_duplicates('aabBcde')) # 2