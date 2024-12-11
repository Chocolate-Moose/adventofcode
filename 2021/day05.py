# day 5: hydrothermal venture
# https://adventofcode.com/2021/day/5

def hydrothermal_venture_one(vents):
    floor = [[0 for _ in range(max(max(x[0]) for x in vents) + 1)] for _ in range(max(max(x[1]) for x in vents) + 1)]

    # fill the floor
    for vent in vents:
        (x0, y0), (x1, y1) = vent
        if x0 == x1:
            for i in range(y0, y1 + 1): floor[x0][i] += 1
        elif y0 == vent[1][1]:
            for i in range(x0, x1 + 1): floor[i][y0] += 1

    # count overlaps
    overlap = 0
    for row in floor:
        for num in row:
            if num > 1: overlap += 1
    print(overlap)

def hydrothermal_venture_two(vents):
    floor = [[0 for _ in range(max(max(x[0]) for x in vents) + 1)] for _ in range(max(max(x[1]) for x in vents) + 1)]

    # fill the floor
    for vent in vents:
        (x0, y0), (x1, y1) = vent
        if x0 == x1:
            for i in range(y0, y1 + 1): floor[x0][i] += 1
        elif y0 == y1:
            for i in range(x0, x1 + 1): floor[i][y0] += 1
        else:
            dx = 1 if x0 < x1 else -1
            dy = 1 if y0 < y1 else -1
            for i in range(abs(x0 - x1) + 1): floor[x0 + i * dx][y0 + i * dy] += 1

    # count overlaps
    overlap = 0
    for row in floor:
        for num in row:
            if num > 1: overlap += 1
    print(overlap)

def hydrothermal_venture_driver():
    input_file = open("input/hydrothermal_venture", 'r')

    # split parts and add to line of vents
    vents = []
    for line in input_file:
        parts = line.split(' -> ')
        start = tuple(int(i) for i in parts[0].split(','))
        end = tuple(int(i) for i in parts[1].split(','))

        # vent is ordered start and end
        vent = (start, end) if start[0] + start[1] < end[0] + end[1] else (end, start)
        vents.append(vent)
    input_file.close()

    # solve the first problem
    hydrothermal_venture_one(vents)

    # solve the second problem
    hydrothermal_venture_two(vents)

hydrothermal_venture_driver()
