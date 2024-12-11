# Red-Nosed Reports
filename = "input/day02"

def is_valid(levels):
    diffs = [levels[i] - levels[i-1] for i in range(1, len(levels))]
    # check if diffs valid and same sign
    return set(diffs).issubset({1, 2, 3}) or set(diffs).issubset({-1, -2, -3})


def part_one():
    valid = 0
    with open(filename, "r") as input_file:
        for line in input_file:
            levels = [int(x) for x in line.split()]
            if is_valid(levels): valid += 1 

    return valid
    
print("part one:", part_one())

def part_two():
    valid = 0
    with open(filename, "r") as input_file:
        for line in input_file:
            levels = [int(x) for x in line.split()]
            for i in range(len(levels)):
                substr = levels[0:i] + levels[i+1:len(levels)]
                if is_valid(substr): 
                    valid += 1 
                    break

    return valid

print("part two:", part_two())
