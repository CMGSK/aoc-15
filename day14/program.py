import re

RACE = 2503
highest = 0
for line in open('input.txt'):
    vel, time, rest = re.findall(r'\d+', line)
    distance = 0
    recovered = False
    i = 0
    while i < RACE:
        if RACE - i > int(time):
            distance += int(vel) * int(time)
            i += int(time) + int(rest)
        else:
            distance += int(vel) * (RACE - i)
            break
    highest = distance if distance > highest else highest
print(highest)
