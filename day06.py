# day 6: custom customs
def custom_customs_one():
    input_file = open('input/custom_customs', 'r')
    answers = set()
    total = 0

    for line in input_file:
        # count number of letters in set
        if line == '\n':
            total += len(answers)
            answers.clear()
        else:
            for char in line.rstrip():
                answers.add(char)
    print(total)

def custom_customs_two():
    input_file = open('input/custom_customs', 'r')
    answers = []
    total = 0
    new_set = True

    for line in input_file:
        if line == '\n':
            # count number of shared answers
            total += len(answers)
            answers.clear()
            new_set = True
        elif new_set:
            # add all characters to answers
            answers = list(line.rstrip())
            new_set = False
        else:
            # union with existing answers -- we loop over a copy of the list here
            for char in list(answers):
                if char not in line:
                    answers.remove(char)
    print(total)
