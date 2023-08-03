import re


def result_sum(input):
    r = 0
    for n in re.findall(r'-?\d+', input):
        r += int(n)
    return r


input = open('input.txt').read()
result = 0
result += result_sum(input)
print('Result 1: ' + str(result))

result2 = 0
while ':"red"' in input:
    for obj in re.findall(r'{[^{}]*}', input):
        replacement = ''
        if ':"red"' in obj:
            replacement = '[0]'
        else:
            replacement = '[' + str(result_sum(obj)) + ']'
        input = input.replace(obj, replacement)
result2 += result_sum(input)
print('Result 2: ' + str(result2))
