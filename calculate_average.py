# def calculate_average(nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     amount = len(nums)
#     if amount > 0:
#         result = sum / amount
#     else:
#         result = sum
#     return result

# def calculate_average(nums):
#     try:
#         return sum(nums) / len(nums)
#     except ZeroDivisionError:
#         return 0

def calculate_average(nums):
    return sum(nums) / len(nums) if nums else 0