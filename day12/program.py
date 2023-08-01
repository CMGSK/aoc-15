import re


def replacer(m):
    json_obj = m.group(0)
    if '":red"' not in json_obj:
        return str(json_obj)
    else:
        return '[0]'


input = open('input.txt')
result = 0
result2 = 0
for line in input:
    for n in re.findall(r'-?\d+', line):
        result += int(n)
print(result)

while ':"red"' in input:
    input = re.sub(r'\{[^{}]*\}', replacer, input)
print(input)
# for line in input:
#     for n in re.findall(r'-?\d+', line):
#         result2 += int(n)
print(result2)
