# day 15: rambunctious recitation
def rambunctious_recitation_one():
    rambunctious_recitation_general(2020)

def rambunctious_recitation_two():
    rambunctious_recitation_general(30000000)

def rambunctious_recitation_general(num_turns):
    starters = open('input/rambunctious_recitation').read().split(',')

    # fill ages with starter numbers
    ## ages = { number: time last spoken }
    ages = { int(x) : i + 1 for i, x in enumerate(starters) if i != len(starters) - 1}
    last_spoken = int(starters[len(starters) - 1])
    turn = len(starters)

    while turn < num_turns:
        # number hasn't been spoken yet
        if last_spoken not in ages:
            ages[last_spoken] = turn
            last_spoken = 0
        else:
            last_time = ages[last_spoken]
            ages[last_spoken] = turn
            last_spoken = turn - last_time
        turn += 1

    print(last_spoken)
