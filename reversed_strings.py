def reverse_string(s):
    str = ""
    for i in list(reversed(s)):
        str += i
        return str


print(reverse_string("123"))