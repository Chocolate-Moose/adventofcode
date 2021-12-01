# day 7: handy haversacks
def handy_haversacks_one():
    input_file = open('input/handy_haversacks', 'r')
    # bag => [things that hold the bag]
    bag_table = {}

    # fill bag table
    for line in input_file:
        split_line = line.split(' ')
        big_bag = split_line[0] + ' ' + split_line[1]

        # the bag doesn't contain other bags
        if len(split_line) == 7: continue

        # add what bag contains to table
        for i in range(5, len(split_line), 4):
            small_bag = split_line[i] + ' ' + split_line[i + 1]
            if small_bag in bag_table:
                bag_table[small_bag].append(big_bag)
            else:
                bag_table[small_bag] = [big_bag]

    # find what bags can hold gold ones
    hold_gold_bags = set()
    to_visit = ['shiny gold']
    # modified BFS over bag_table
    while to_visit:
        new_bag = to_visit.pop(0)
        # if this bag can be fit in another bag, add bigger bags
        if new_bag in bag_table:
            to_visit.extend(bag_table[new_bag])
        hold_gold_bags.add(new_bag)
    print(len(hold_gold_bags) - 1) # subtract 1 bc gold bag is in set

def handy_haversacks_two():
    input_file = open('input/handy_haversacks', 'r')
    # bag => [bags that it fits => number that go inside]
    bag_table = {}

    for line in input_file:
        split_line = line.split(' ')
        big_bag = split_line[0] + ' ' + split_line[1]
        bag_table[big_bag] = {}

        # the bag doesn't contain other bags
        if len(split_line) == 7: continue

        # add what bag contains to table
        for i in range(5, len(split_line), 4):
            small_bag = split_line[i] + ' ' + split_line[i + 1]
            number = split_line[i - 1]
            bag_table[big_bag][small_bag] = number

    # we subtract 1 to account for counting
    # the gold bag in the recursive helper method
    total_bags = fill_bag(bag_table, 'shiny gold') - 1
    print(total_bags)

# recursive method to find inner bags
def fill_bag(bag_table, cur_bag):
    # the bag holds 0 bags
    if not bag_table[cur_bag]:
        return 1
    # sum the inner bags
    total = 1
    for inner_bag in bag_table[cur_bag]:
        total += int(bag_table[cur_bag][inner_bag]) * fill_bag(bag_table, inner_bag)
    return total
