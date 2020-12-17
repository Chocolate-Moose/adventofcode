# day 9: encoding error
def encoding_error_one():
    nums = open('input/encoding_error').read().split('\n')

    # keep track of previous 25 numbers
    preamble = set()
    preamble.update(nums[:25])

    for i, num in enumerate(nums[25:], 25):
        # break if number isn't sum of previous
        for j, pre in enumerate(preamble):
            if str(int(num) - int(pre)) in preamble and pre != int(num) / 2:
                break
            if j == len(preamble) - 1:
                print(num)
                quit()

        # update preamble
        preamble.remove(nums[i - 25])
        preamble.add(num)

# use sliding window approach :)
# runtime: O(n)
def encoding_error_two():
    # learning new things
    nums = list(map(int, open('input/encoding_error').read().split('\n')))

    start, total, end = 0, 0, 0
    # make window bigger/smaller based on current totals
    while end < len(nums) - 1:
        if total < 167829540:
            total += nums[end]
            end += 1
        elif total > 167829540:
            total -= nums[start]
            start += 1
        else:
            break

    # sum largest and smallest in subarray
    print(max(nums[start:end]) + min(nums[start:end]))
