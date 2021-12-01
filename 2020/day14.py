# day 14: docking data
# these two were a doozy
def charlie_big_poggers():
    input_file = open('input/docking_data')

    masked_zeros, masked_ones, memory = 0, 0, {}
    for line in input_file:
        split = line.rstrip().replace(' ', '').split('=')

        # keep track of 0, 1 in mask
        if split[0] == 'mask':
            # crazy replacing because there's no better way to flip bits
            masked_zeros = int(split[1].replace('X', '1').replace('0', '2').replace('1', '0').replace('2', '1'), 2)
            masked_ones = int(split[1].replace('X', '0'), 2)

        # mask number and add to spot in memory
        # or, minus takes care of 0's in mask, or takes care of 1's in mask
        else:
            value = int(split[1])
            value = ((value | masked_zeros) - masked_zeros) | masked_ones
            location = split[0][(split[0].find('[') + 1):(split[0].find(']'))]
            memory[location] = value

    # loop through memory and sum totals
    total = 0
    for key in memory:
        total += memory[key]

    print(total)

def charlie_so_nice_and_notz_ogre_bonkz_bomn():
    input_file = open('input/docking_data')

    masked_ones, masked_xs, num_x, x_loc, memory = 0, 0, 0, [], {}
    for line in input_file:
        split = line.rstrip().replace(' ', '').split('=')

        if split[0] == 'mask':
            masked_ones = int(split[1].replace('X', '0'), 2)
            masked_xs = int(split[1].replace('1', '0').replace('X', '1'), 2)
            x_loc = [i for i, x in enumerate(reversed(split[1])) if x == 'X']
            num_x = split[1].count('X')

        else:
            location = int(split[0][(split[0].find('[') + 1):(split[0].find(']'))])
            # override the 1's and zero out the X's
            location = ((location | masked_xs) - masked_xs) | masked_ones

            # cycle through binary numbers to find all combos of X's
            for i in range(0, 2 ** num_x):
                switch = str(bin(i)[2:])
                new_location = location

                # add the x's
                for loc, x in enumerate(x_loc):
                    if loc < len(switch):
                        new_location += (2 ** x) * int(switch[::-1][loc])
                    else: break
                memory[new_location] = int(split[1])

    # loop through memory and sum totals
    total = 0
    for key in memory:
        total += memory[key]

    print(total)
