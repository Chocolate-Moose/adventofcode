# day 2: password philosophy
def password_philosophy_one():
    input_file = open('input/password_philosophy', 'r')
    correct = 0

    # parse each line and see if password is correct
    for line in input_file:
        first_split = line.split('-')
        low = int(first_split[0])
        second_split = first_split[1].split(' ')
        high = int(second_split[0])
        thechar = (second_split[1])[0]
        password = second_split[2]

        if low <= password.count(thechar) <= high:
            correct += 1
    print(correct)


def password_philosophy_two():
    input_file = open('input/password_philosophy', 'r')
    correct = 0

    for line in input_file:
        first_split = line.split('-')
        low = int(first_split[0]) - 1
        second_split = first_split[1].split(' ')
        high = int(second_split[0]) - 1
        thechar = (second_split[1])[0]
        password = second_split[2]

        if (password[low] == thechar and password[high] != thechar) \
                or (password[low] != thechar and password[high] == thechar):
            correct += 1
    print(correct)
