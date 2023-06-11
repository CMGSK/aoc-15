import re


def contains_vowels(line):
    vowels = 'a', 'e', 'i', 'o', 'u'
    r = 0
    for c in line:
        if c in vowels:
            r += 1
    if r >= 3:
        return True
    else:
        return False


def no_consec(line):
    pairs = "ab", "cd", "pq", "xy"
    if any(pair in line for pair in pairs):
        return False
    else:
        return True


def has_reps(line):
    char = ' '
    for c in line:
        if c == char:
            return True
        char = c
    return False


# Originally I wanted to parse these problems to get comfy with python
# but ain't doing second part by manual parsing LOL
def double_rep(line):
    pair_rep = r"(\w\w).*\1"
    couple_split = r"(\w)\w\1"
    if re.search(pair_rep, line) is None or re.search(couple_split, line) is None:
        return False
    else:
        return True


file = open("input.txt")
part1 = 0
part2 = 0
for line in file:
    if contains_vowels(line) and no_consec(line) and has_reps(line):
        part1 += 1
    if double_rep(line):
        part2 += 1
print(part1)
print(part2)
