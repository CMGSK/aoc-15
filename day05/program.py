file = open("input.txt")


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


part1 = 0
for line in file:
    vowels = contains_vowels(line)
    consecution = no_consec(line)
    repetition = has_reps(line)
    if vowels and consecution and repetition:
        part1 += 1
print(part1)
