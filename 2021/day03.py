# day 3: binary diagnostic
# https://adventofcode.com/2021/day/3

def binary_diagnostic_one(diagnostic):
    counts = [0] * len(diagnostic[0])

    # get counts of 1 for each position
    for number in diagnostic:
        for i, digit in enumerate(number):
            if digit == '1': counts[i] += 1

    # make epsilon and gamma
    epsilon = gamma = 0
    for i, count in enumerate(counts):
        # more than half are 1
        if count > len(diagnostic) // 2: epsilon += 2 ** (len(diagnostic[0]) - i - 1)
        # more than half are 0
        else: gamma += 2 ** (len(diagnostic[0]) - i - 1)

    print(epsilon * gamma)

def binary_diagnostic_two(diagnostic):
    o2 = bit_criteria(diagnostic.copy(), 'o2')
    co2 = bit_criteria(diagnostic.copy(), 'co2')

    print(int(o2, 2) * int(co2, 2))

def bit_criteria(diagnostic, type):
    pos = 0
    while len(diagnostic) > 1:
        count = 0
        # get count of 1 in this position
        for num in diagnostic:
            if num[pos] == '1': count += 1

        # remove all values that don't pass filter
        filtered = []

        # in majority or minority based on type of rating
        if type == 'o2': to_remove = '1' if count < len(diagnostic) / 2 else '0'
        else: to_remove = '0' if count < len(diagnostic) / 2 else '1'

        for num in diagnostic:
            if num[pos] != to_remove: filtered.append(num)

        # increment and reset variables
        diagnostic = filtered
        pos += 1

    return diagnostic[0]

# might've gone a little overboard with all the methods
def binary_diagnostic_driver():
    input_file = open('input/binary_diagnostic', 'r')
    diagnostic = []

    for line in input_file:
        diagnostic.append(line.strip())
    input_file.close()

    # solve the first problem
    binary_diagnostic_one(diagnostic)

    # solve the second problem
    binary_diagnostic_two(diagnostic)

binary_diagnostic_driver()