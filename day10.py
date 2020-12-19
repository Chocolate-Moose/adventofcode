# day 10: adapter array
def adapter_array_one():
    adapters = list(map(int, open('input/adapter_array').read().split('\n')))
    adapters.append(0)     # initial port
    adapters.sort()

    differences = [0, 0, 0]
    for i in range(1, len(adapters)):
        differences[adapters[i] - adapters[i - 1] - 1] += 1

    print(differences[0] * (differences[2] + 1))

def adapter_array_two():
    adapters = list(map(int, open('input/adapter_array').read().split('\n')))
    adapters = [0] + sorted(adapters)

    diffs = ''
    for i, adapter in enumerate(adapters[1:], 1):
        diffs += str(adapters[i] - adapters[i - 1])

    # differences of 1 next to each other increase total possibilities
    fours = diffs.count('1111')
    threes = diffs.count('111') - fours
    twos = diffs.count('11') - threes - 2 * fours
    print(7 ** fours * 4 ** threes * 2 ** twos)
