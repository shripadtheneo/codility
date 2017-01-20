"""
Assume the input is an array of numbers 0 and 1. Here, a "Same Value Part Array" means a part of
an array in which successive numbers are the same.

For example, "11", "00" and "111" are all "Same Value Part Arrays" but "01" and "10" are not.

Given Above, implement a program to return the longest "Same Value Part Array" for any array
input. e.g. "011011100"
"""


def long_same_part_arr(sequence):
    longest = (0, 0)
    curr = (0, 0)
    first, last = 0, 0
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            last = i
            curr = first, last
        else:
            first, last = i, i
        if curr[1] - curr[0] > longest[1] - longest[0]:
            longest = curr

    return sequence[longest[0]:longest[1] + 1]


if __name__ == '__main__':
    sequence = "01101110000"
    print (long_same_part_arr(sequence))
