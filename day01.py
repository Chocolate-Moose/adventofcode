# day 1: report repair
# runtime: O(n)
def report_repair_one():
    # make set to store numbers
    numbers = set()

    # add numbers in file to set
    input_file = open("input/report_repair", 'r')
    for line in input_file:
        num = int(line)
        if (2020 - num) in numbers:
            print((2020 - num) * num)
            return 
        numbers.add(num)

# runtime: O(n^2)
def report_repair_two():
    # add everything to numbers list
    number_list = []
    input_file = open("input/report_repair", 'r')
    for line in input_file:
        number_list.append(int(line))

    # similar approach to first, but trying all combos of 2 numbers
    numbers = set()
    for i in range(0, len(number_list)):
        for j in range(i + 1, len(number_list)):
            one = number_list[i]
            two = number_list[j]
            if (2020 - one - two) in numbers:
                print(one * two * (2020 - one - two))
                return
            numbers.add(one)
