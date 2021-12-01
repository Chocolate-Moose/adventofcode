# day 3: toboggan trajectory
# need to make sure last line has one extra character
def toboggan_trajectory_one():
    input_file = open('input/toboggan_trajectory', 'r')
    trees = 0
    line_num = 0

    for line in input_file:
        index = (line_num * 3) % (len(line) - 1)  # for some reason there's an extra space from copy/paste
        if line[index] == '#':
            trees += 1
        line_num += 1
    print(trees)


def toboggan_trajectory_two():
    one = toboggan_trajectory_two_helper(1, 1)
    two = toboggan_trajectory_two_helper(3, 1)
    three = toboggan_trajectory_two_helper(5, 1)
    four = toboggan_trajectory_two_helper(7, 1)
    five = toboggan_trajectory_two_helper(1, 2)
    print(one * two * three * four * five)


def toboggan_trajectory_two_helper(dx, dy):
    input_file = open('input/toboggan_trajectory', 'r')
    trees = 0
    line_num = 0

    for line in input_file:
        if line_num % dy == 0:
            index = int(((line_num / dy) * dx) % (len(line) - 1))
            if line[index] == '#':
                trees += 1
        line_num += 1
    return trees
