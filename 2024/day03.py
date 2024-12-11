# Mull It Over
import re

filename = "input/day03"

def parse_input(pattern):
    with open(filename, "r") as input_file:
        line = input_file.read().strip()
        return re.findall(pattern, line)


def part_one():
        matches = parse_input( "mul\((\d+),(\d+)\)")
        return sum([int(x) * int(y) for (x, y) in matches])
            
print("part one:", part_one())

def part_two():
    with open(filename, "r") as input_file:
        line = input_file.read().strip()
        pattern = "mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
        matches = re.findall(pattern, line)
        
        keep = True
        sum = 0
        for x, y, do, dont in matches:
            if dont: keep = False
            elif do: keep = True
            else: sum += int(x) * int(y) * keep
        return sum

print("part two:", part_two())       

