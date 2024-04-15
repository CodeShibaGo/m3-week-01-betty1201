def array_diff(a, b):
    return [x for x in a if x not in b]

# def array_diff(a, b):
#     array_diff_list = []
#     for x in a:
#         if x not in b:
#             array_diff_list.append(x)
#     return array_diff_list