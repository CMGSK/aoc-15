# data = '3113322113'
# result = ''
# for i in range(50):
#     for e in range(len(data)):
#         if data[e] == data[e - 1] and e != 0:
#             continue
#         counter = 1
#         actual = data[e]
#         while e + 1 < len(data) and data[e + 1] == data[e]:
#             e += 1
#             counter += 1
#         result += str(counter) + actual
#     data = result
#     result = ''
#     if i == 39:
#         print(len(data))
# print(len(data))

# Optimization attempt

# import re
#
# data = '3113322113'
# pattern = re.compile(r"(\d)\1*")
#
# for i in range(50):
#     data = re.sub(pattern, str(, data)
#     if i == 40:
#         print(data)
# print(len(data))
#

# Second optimization attempt

import re


def replace(m):
    s = m.group(0)
    return str(len(s)) + s[0]


reg = re.compile(r'(\d)\1*')
s = '3113322113'
for i in range(50):
    s = reg.sub(replace, s)
    # here, sub expects a function as first argument, and the function infers the parameter expected, taking the
    # second argument. This part I had to look it up
    if i == 40:
        print('Part 1: ' + str(len(s)))
print('Part 2: ' + str(len(s)))
