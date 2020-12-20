# day 11: seating system
def seating_system_one():
    seating_system_general(filled_neighbors, 4)

def seating_system_two():
    seating_system_general(filled_visible_neighbors, 5)

def seating_system_general(count_neighbors, neighbor_limit):
    input_file = open('input/seating_system', 'r')
    seats = []

    # add inputs into 2d array
    for row in input_file:
        temp = list(row.rstrip())
        seats.append(temp)

    # simulate seating rules
    change = True
    while change:
        change = False
        new_seats = copy.deepcopy(seats)

        # loop through seats and do the changes
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                if seats[i][j] == '.': continue

                filled = count_neighbors(seats, i, j)
                if filled >= neighbor_limit and seats[i][j] == '#': new_seats[i][j] = 'L'
                if filled == 0 and seats[i][j] == 'L': new_seats[i][j] = '#'
                if new_seats[i][j] != seats[i][j]: change = True

        seats = new_seats

    print(sum(row.count('#') for row in seats))

# counts neighbors for pt 1
def filled_neighbors(seats, row, col):
    filled = 0
    for i in range(max(0, row - 1), min(row + 1, len(seats) - 1) + 1):
        for j in range(max(0, col - 1), min(col + 1, len(seats[0]) - 1) + 1):
            if seats[i][j] == '#' and (i != row or j != col): filled += 1
    return filled

# counts neighbors for pt 2
def filled_visible_neighbors(seats, row, col):
    filled = 0
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]

    # loop over all the directions to find filled seats
    for dx, dy in directions:
        i, j = row + dx, col + dy
        while 0 <= i <= len(seats) - 1 and 0 <= j <= len(seats[0]) - 1:
            if seats[i][j] == 'L': break
            if seats[i][j] == '#':
                filled += 1
                break
            i += dx
            j += dy
    return filled
