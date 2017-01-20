"""
Assume the input is an array of numbers 0 and 1. Here, a "Same Value Part Array" means a part of
an array in which successive numbers are the same.

For example, "11", "00" and "111" are all "Same Value Part Arrays" but "01" and "10" are not.

Given Above, implement a program to return the longest "Same Value Part Array" for any array
input. e.g. "011011100"
"""


def long_same_part_arr(sequence):
    length = len(sequence)
    longest_arr = []
    inter_arr = [sequence[0]]

    return longest_arr


if __name__ == '__main__':
    sequence = "011011100"
    print (long_same_part_arr(sequence))
