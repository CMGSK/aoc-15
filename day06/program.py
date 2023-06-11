# once again, not parsing text like im a caveman
import re

file = open("input.txt")
grid = [[False] * 1000 for i in range(0, 1000)]  # Creating a 1000x1000 boolean 2D array False by default
grid_correction = [[0] * 1000 for j in range(0, 1000)]
for line in file:
    pattern = r"\d+"
    digits = list(map(int, re.findall(pattern, line)))  # Converting from str to int[] in the same line
    # Do not forget that second parameter in range is exclusive, so we need to add an additional instruction there
    if "toggle" in line:
        for i in range(digits[0], digits[2] + 1):
            for j in range(digits[1], digits[3] + 1):
                grid[i][j] = not grid[i][j]
                grid_correction[i][j] += 2
    else:
        for i in range(digits[0], digits[2] + 1):
            for j in range(digits[1], digits[3] + 1):
                grid[i][j] = True if "turn on" in line else False
                if "turn on" in line:
                    grid_correction[i][j] += 1
                else:
                    grid_correction[i][j] -= 1 if grid_correction[i][j] > 0 else 0
                    # doing it with not 0 would output a wrong result...

part1 = 0
part2 = 0
for arr in grid:
    for boolean in arr:
        if boolean:
            part1 += 1
for arr in grid_correction:
    for n in arr:
        part2 += n
print(part1)
print(part2)
