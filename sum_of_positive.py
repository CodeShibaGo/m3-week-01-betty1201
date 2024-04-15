# def positive_sum(arr):
#     result = 0
#     for i in arr:
#         if i > 0:
#             result += i
#     return result

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

