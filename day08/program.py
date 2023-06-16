import re

file = open("input.txt")
code = 0
lit = 0
for line in file:
    code = len(line.strip())
    patternHex = r"\\x\w\w"
    patternSla = r"\\\W"
    m = len(re.findall(patternHex, line))
    n = len(re.findall(patternSla, line))
    lit = (len(line.strip()) - (2 + (m*4) + (n*2))) + (m+n)
print(code - lit)