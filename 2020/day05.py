# day 5: binary boarding
def binary_boarding_one():
    input_file = open('input/binary_boarding', 'r')
    max_id = 0

    for line in input_file:
        line = line.rstrip()
        row = airplane_search(line[:7], 0, 127)
        col = airplane_search(line[7:11], 0, 7)
        if (row * 8) + col > max_id:
            max_id = (row * 8) + col

    print(max_id)

# modified binary search
def airplane_search(seat, p, q):
    # base case
    if len(seat) == 0 or p == q:
        return p
    # take lower half
    if seat[0] == 'F' or seat[0] == 'L':
        return airplane_search(seat[1:], p, (p + q - 1) / 2)
    # take upper half
    else:
        return airplane_search(seat[1:], (p + q + 1) / 2, q)

def binary_boarding_two():
    input_file = open('input/binary_boarding', 'r')
    seats = {r: [] for r in range(0, 128)}
    ids = set()

    # read all boarding passes nearby
    for line in input_file:
        line = line.rstrip()
        row = airplane_search(line[:7], 0, 127)
        col = airplane_search(line[7:11], 0, 7)
        seats[row].append(col)
        ids.add((row * 8) + col)

    # find missing seat
    for row in seats:
        if len(seats[row]) == 7:
            missing = 28 - sum(seats[row])
            new_id = (row * 8) + missing
            if (new_id + 1) in ids and (new_id - 1) in ids:
                print(new_id)
