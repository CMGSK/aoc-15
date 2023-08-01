from itertools import permutations
from collections import defaultdict


# For each both cities in permutation
def total(list):
    # Had to look the zip thing up and the defaultdict structure bc coulndt find how to do what i had in mind
    return sum(cities[fc][sc] for fc, sc in zip(list, list[1:]))


file = open("input.txt")
cities = defaultdict(dict)

for line in file:
    line = line.strip().split(' ')
    fc, _, sc, _, dist = line
    cities[fc][sc] = int(dist)
    cities[sc][fc] = int(dist)

results = [total(e) for e in permutations(cities.keys())]
print('Min result: ' + str(min(results)))
print('Max result: ' + str(max(results)))
