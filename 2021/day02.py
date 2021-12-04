# day 2: dive!
# https://adventofcode.com/2021/day/2

def dive_one():
    input_file = open('input/dive', 'r')

    x = y = 0
    for line in input_file:
        split = line.split(' ')
        if split[0] == 'forward': x += int(split[1])
        elif split[0] == 'down': y += int(split[1])
        elif split[0] == 'up': y -= int(split[1])

    input_file.close()
    print(x * y)

dive_one()


def dive_two():
    input_file = open('input/dive', 'r')

    x = y = aim = 0
    for line in input_file:
        split = line.split(' ')
        if split[0] == 'forward':
            x += int(split[1])
            y += aim * int(split[1])
        elif split[0] == 'down': aim += int(split[1])
        elif split[0] == 'up': aim -= int(split[1])

    input_file.close()
    print(x * y)

dive_two()