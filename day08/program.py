import re

file = open("input.txt")
code = 0
lit = 0
pat = 0
pattern = r"[\\\"]"
for line in file:
    code += len(line.strip())
    lit += len(eval(line))
    pat += len(line.strip()) + 2 + len(re.findall(pattern, line))
print(code-lit)
print(pat-code)
