import re
from collections import defaultdict
from itertools import permutations


# Create our collection
data = defaultdict(dict)
# Parse it into the correct data
for line in open('input.txt'):
    x = re.match(r'(\w+) \w+ (gain|lose) (\d+) (?:\w+ ){6}(\w+)', line)
    p1, operator, number, p2 = x.groups()
    data[p1][p2] = int(number) if operator == 'gain' else -int(number)


def happiness_calc(data):
    highest = 0
    # Parse all permutations taking care of both sides of the seat, and return the highest found
    for option in permutations(data.keys()):
        happiness = sum(data[x][y] + data[y][x] for x, y in zip(option, option[1:]))
        happiness += data[option[0]][option[-1]] + data[option[-1]][option[0]]
        highest = max(highest, happiness)
    return highest

print(happiness_calc(data))

# Adding ourselves to the equation for the permutations to calculate again
for person in list(data.keys()):
    data['Myself'][person] = 0
    data[person]['Myself'] = 0

print(happiness_calc(data))
