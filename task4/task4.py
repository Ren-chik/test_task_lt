import random
import sys


def get_nums(filename):
    with open(filename, 'r') as file:
        nums = [int(i.strip()) for i in file.readlines()]
    return nums


def get_least_steps(nums):
    median = quickselect_median(nums)
    if isinstance(median, tuple):
        return min(sum(abs(i - median[0]) for i in nums), sum(abs(i - median[1]) for i in nums))
    else:
        return sum(abs(i - median) for i in nums)


def quickselect_median(nums):
    if len(nums) % 2 == 1:
        return quickselect(nums, len(nums) / 2)
    else:
        return quickselect(nums, len(nums) / 2 - 1), quickselect(nums, len(nums) / 2)


def quickselect(nums, k):
    if len(nums) == 1:
        return nums[0]

    pivot = random.choice(nums)

    lows = [el for el in nums if el < pivot]
    highs = [el for el in nums if el > pivot]
    equals = [el for el in nums if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(equals):
        return equals[0]
    else:
        return quickselect(highs, k - len(lows) - len(equals))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    filename = sys.argv[1]

    nums = get_nums(filename)

    result = get_least_steps(nums)

    print(result)
