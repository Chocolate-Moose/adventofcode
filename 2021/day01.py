# day 1: sonar sweep
# https://adventofcode.com/2021/day/1

def sonar_sweep_one():
    input_file = open("input/sonar_sweep", 'r')

    num_increase = 0
    prev = float('inf')
    # compare every number to previous and update previous
    for line in input_file:
        if int(line) > prev:
            num_increase += 1
        prev = int(line)

    input_file.close()
    print(num_increase)

sonar_sweep_one()

def sonar_sweep_two():
    input_file = open("input/sonar_sweep", 'r')

    depths = []
    # put numbers in an array
    for line in input_file:
        depths.append(int(line))
    input_file.close()

    num_increase = 0
    sums = 0
    # sliding window sums over depths
    for i, depth in enumerate(depths):
        # sum the first 3 numbers
        if i < 3:
            sums += depth
        # slide the window and compare
        else:
            new_sum = sums + depth - depths[i - 3]
            if new_sum > sums: num_increase += 1
            sums = new_sum
    print(num_increase)

sonar_sweep_two()