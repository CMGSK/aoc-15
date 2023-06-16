file = open("input.txt")


def r_find_val(instructions, process):
    if process.isnumeric():
        return int(process)
    p = instructions[process]
    if isinstance(instructions[process], str):
        if not p.isnumeric():
            if "NOT" in p:
                instructions[process] = ~r_find_val(instructions, p[4:]) & 0xFFFF
            elif "OR" in p:
                wires = p.split(" OR ")
                instructions[process] = r_find_val(instructions, wires[0]) | r_find_val(instructions, wires[1])
            elif "AND" in p:
                wires = p.split(" AND ")
                instructions[process] = r_find_val(instructions, wires[0]) & r_find_val(instructions, wires[1])
            elif "LSHIFT" in p:
                wires = p.split(" LSHIFT ")
                instructions[process] = r_find_val(instructions, wires[0]) << int(wires[1])
            elif "RSHIFT" in p:
                wires = p.split(" RSHIFT ")
                instructions[process] = r_find_val(instructions, wires[0]) >> int(wires[1])
        else:
            return int(instructions[process])
    if isinstance(instructions[process], int):
        return instructions[process]


instructions = {}
for line in file:
    data = line.split(" -> ")
    instructions[data[1][:-1]] = data[0]
part2 = instructions.copy()
result = r_find_val(instructions, instructions["a"])
print("part 1: " + str(result))
part2["b"] = result
result = r_find_val(part2, part2["a"])
print("part 2: " + str(result))
