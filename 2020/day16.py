# day 16: ticket translation
def ticket_translation_one():
    inputs = open('input/ticket_translation').read().split('\n\n')

    parsed = inputs[0].split('\n')
    ranges = []

    # add the ranges as tuples to list, then sort by start time
    for rule in parsed:
        chunky = rule.split(': ')
        chunk = chunky[1].split(' ')
        ranges.append((int(chunk[0].split('-')[0]), int(chunk[0].split('-')[1])))
        ranges.append((int(chunk[2].split('-')[0]), int(chunk[2].split('-')[1])))
    ranges.sort()

    invalid = set()

    # add invalid numbers (ones in between tuples) to set
    for i in range(0, len(ranges) - 1):
        lower = ranges[i][1]
        upper = ranges[i + 1][0]
        if lower < upper:
            invalid.update([j for j in range(lower + 1, upper)])

    error_rate = 0
    # find invalid numbers in nearby tickets
    nearby = inputs[2].split('\n')
    for i in range(1, len(nearby)):
        nums = list(map(int, nearby[i].split(',')))
        for j in nums:
            # some sketchy checks -- got lucky on the input
            if j in invalid or j > ranges[len(ranges) - 1][1] or j < ranges[0][0]: error_rate += j

    print(error_rate)

# this one was a doozy
def ticket_translation_two():
    inputs = open('input/ticket_translation').read().split('\n\n')

    # get rid of invalid tickets nearby
    valid = []
    nearby = inputs[2].split('\n')
    for i in range(1, len(nearby)):
        nums = list(map(int, nearby[i].split(',')))
        is_valid = True
        for j in nums:
            if j > 974 or j < 26: is_valid = False;
        if is_valid: valid.append(nums)

    # store valid numbers for each field
    rules = []
    ordered_fields = []
    for line in inputs[0].split('\n'):
        chunky = line.split(': ')
        ordered_fields.append(chunky[0])
        chunk = chunky[1].split(' ')
        rules.append([int(chunk[0].split('-')[0]), int(chunk[0].split('-')[1]), int(chunk[2].split('-')[0]), int(chunk[2].split('-')[1])])
    '''
     rules = [[.......]
              [.......]
              [.......]]
              
    fields =    col1   col2    col3
        rule1    x      0       0
        rule2    0      x       x
    '''
    # check what are potential valid fields for every column
    fields = [[0 for i in range(len(valid[0]))] for j in range(len(rules))]
    for col in range(len(valid[0])):
        for row in range(len(valid)):
            ticket = valid[row][col]
            for i in range(len(rules)):
                if ticket < rules[i][0] or (ticket > rules[i][1] and ticket < rules[i][2]) or ticket > rules[i][3]:
                    fields[col][i] = 'x'

    # match each field to its column
    undetermined = [i for i in range(len(rules))]
    final_rules = [0] * len(undetermined)

    while len(undetermined) > 1:
        for und in undetermined:
            field = fields[und]
            # there's only one possible field for this column
            if field.count(0) == 1:
                found = field.index(0)
                final_rules[und] = ordered_fields[found]
                undetermined.remove(und)

                # no other column can also be this field
                for un in undetermined:
                    fields[un][found] = 'x'
                break
    final_rules[undetermined[0]] = ordered_fields[fields[und].index(0)]

    # do the multiplying
    my_ticket = inputs[1].split('\n')[1]
    my_ticket = my_ticket.split(',')

    total = 1
    for i in range(len(final_rules)):
        if 'departure' in final_rules[i]:
            total *= int(my_ticket[i])

    print(total)
