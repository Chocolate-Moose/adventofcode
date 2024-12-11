# Historian Histeria
import array 

filename = "input/day01"

def read_input():
    left = []
    right = []

    with open(filename, "r") as input_file:
        for line in input_file:
            parts = line.split()
            left.append(int(parts[0]))
            right.append(int(parts[1]))

    return left, right

def part_one():
    left, right = read_input()

    # sort left and right
    left.sort()
    right.sort()

    # compare
    return sum(abs(i - j) for i, j in zip(left, right))

print("part one:", part_one())

def part_two():
    left, right = read_input()
    right_counts = {x:right.count(x) for x in right}
    
    return sum(0 if i not in right_counts else i * right_counts[i] for i in left)

print("part two:", part_two())