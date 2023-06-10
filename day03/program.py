file = open("input.txt")
houses = file.read()


def part1(houses):
    actual = (0, 0)
    visits = {(0,0)} #cannot use Set() since it uses an iterable and result will be +1
    for house in houses:
        if house == '^':
            actual = (actual[0] + 1, actual[1])
            visits.add(actual)
        if house == '>':
            actual = (actual[0], actual[1] + 1)
            visits.add(actual)
        if house == '<':
            actual = (actual[0], actual[1] - 1)
            visits.add(actual)
        if house == 'v':
            actual = (actual[0] - 1, actual[1])
            visits.add(actual)
    print(len(visits))


def part2(houses):
    santa = (0, 0)
    robot = (0, 0)
    visits = {(0,0)}
    is_santa = False
    for house in houses:
        is_santa = not is_santa
        if is_santa:
            if house == '^':
                santa = (santa[0] + 1, santa[1])
                visits.add(santa)
            if house == '>':
                santa = (santa[0], santa[1] + 1)
                visits.add(santa)
            if house == '<':
                santa = (santa[0], santa[1] - 1)
                visits.add(santa)
            if house == 'v':
                santa = (santa[0] - 1, santa[1])
                visits.add(santa)
        else:
            if house == '^':
                robot = (robot[0] + 1, robot[1])
                visits.add(robot)
            if house == '>':
                robot = (robot[0], robot[1] + 1)
                visits.add(robot)
            if house == '<':
                robot = (robot[0], robot[1] - 1)
                visits.add(robot)
            if house == 'v':
                robot = (robot[0] - 1, robot[1])
                visits.add(robot)
    print(len(visits))


part1(houses)
part2(houses)
