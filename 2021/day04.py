# day 4: giant squid
# https://adventofcode.com/2021/day/4

def giant_squid_one(drawn, boards):
    # loop over every drawn number
    for draw in drawn:
        # loop over every board
        for j, board in enumerate(boards):
            # if the number is in the board, mark it
            for i, number in enumerate(board):
                if number == draw:
                    board[i] = -1
                    # check if the board has won
                    if bingo(board):
                        print(tally_score(board) * draw)
                        return
                    break

# pretty hardcoded function because I know the size of the board
def bingo(board):
    # loop over row
    for i in range(0, len(board), 5):
        if board[i] == board[i + 1] == board[i + 2] == board[i + 3] == board[i + 4] == -1:
            return True

    # loop over column
    for i in range(0, 5):
        if board[i] == board[i + 5] == board[i + 10] == board[i + 15] == board[i + 20] == -1:
            return True

    # no bingo :(
    return False

def tally_score(board):
    total = 0
    for number in board:
        if number != -1: total += number
    return total

def giant_squid_two(drawn, boards):
    # loop over every drawn number
    for draw in drawn:
        print(draw)
        to_remove = []
        # loop over every board
        for j, board in enumerate(boards):
            # if the number is in the board, mark it
            for i, number in enumerate(board):
                if number == draw:
                    board[i] = -1
                    # check if the board has won
                    if bingo(board):
                        to_remove.append(j)
                        # last board has won
                        if len(boards) == 1:
                            print(tally_score(board) * draw)
                            return
                    break
        # remove boards that won
        for num in to_remove[::-1]:
            boards.pop(num)

def giant_squid_driver():
    # read in input file
    input_file = open('input/giant_squid', 'r')
    first = True
    drawn, boards, cur_board = [], [], []

    for line in input_file:
        # store drawn numbers in list
        if first:
            drawn = [int(x) for x in line.split(',')]
            first = False
        # store current board in list of boards
        elif len(cur_board) == 25:
            boards.append(cur_board)
            cur_board = []
        # accumulate numbers in current board
        elif line != '\n':
            cur_board.extend([int(x.strip()) for x in line.split(' ') if x != ''])
    # add the last board to list
    boards.append(cur_board)

    # solve the first problem
    giant_squid_one(drawn, boards)

    # solve the second problem
    giant_squid_two(drawn, boards)

giant_squid_driver()