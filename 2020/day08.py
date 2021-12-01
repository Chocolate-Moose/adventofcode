# day 8: handheld halting
def handheld_halting_one():
    # put commands into list
    # I just discovered you can do it like this instead of using a for loop
    commands = open('input/handheld_halting').read().split('\n')

    accumulator = run_boot_code(commands)[0]
    print(accumulator)

def run_boot_code(commands):
    curr = 0
    accumulator = 0
    visited = set()
    # keep executing commands until we revisit one
    while curr not in visited:
        visited.add(curr)
        # we made it to the end, no loops
        if curr > len(commands) - 1:
            break

        split = commands[curr].split(' ')
        if split[0] == 'acc':
            accumulator += int(split[1])
            curr += 1
        if split[0] == 'jmp':
            curr += int(split[1])
        if split[0] == 'nop':
            curr += 1

    # so we know if this fixed infinite loop in pt 2
    return accumulator, curr > len(commands) - 1

def handheld_halting_two():
    commands = open('input/handheld_halting').read().split('\n')

    # woah!! fancy!!
    # swaps all possible lines
    for command in enumerate(commands):
        split = command[1].split(' ')
        new_commands = commands.copy()

        if split[0] == 'nop':
            new_commands[command[0]] = 'jmp ' + split[1]
        if split[0] == 'jmp':
            new_commands[command[0]] = 'nop ' + split[1]

        res = run_boot_code(new_commands)
        if res[1]:
            print(res[0])
