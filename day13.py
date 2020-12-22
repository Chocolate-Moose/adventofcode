# day 13: shuttle search
def shuttle_search_one():
    # store inputs in variables, ignore out of service shuttles
    with open('input/shuttle_search') as file:
        arrival = int(file.readline().rstrip())
        shuttles = list(map(int, file.readline().rstrip().replace('x,', '').split(',')))

    id, min_wait = 0, 1500000
    # calculate wait time
    for shuttle in shuttles:
        wait_time = shuttle - (arrival % shuttle)
        if wait_time < min_wait:
            min_wait = wait_time
            id = shuttle
    print(id * min_wait)

def charlie_is_so_smart_and_the_best():
    shuttles = open('input/shuttle_search').readlines()[1].split(',')

    offset = {}

    # keep track of offsets for each bus
    for i, shuttle in enumerate(shuttles):
        if shuttle != 'x':
            offset[int(shuttle)] = int(i)

    only_the_shuttles = list(map(int, [i for i in shuttles if i != 'x']))

    curr = only_the_shuttles[0]
    jump = curr
    isDone = False
    next = only_the_shuttles[1]

    while not isDone:
        # if the next number is the correct offset, we can jump by multiples
        if (curr + offset[next]) % next == 0:
            jump *= next
            # if there are more shuttles, continue
            if not only_the_shuttles.index(next) == len(only_the_shuttles) - 1:
                next = only_the_shuttles[only_the_shuttles.index(next) + 1]
            else:
                isDone = True
        # else keep looking
        else: curr += jump

    print(curr)
