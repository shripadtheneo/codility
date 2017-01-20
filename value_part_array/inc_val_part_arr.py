"""
Assume the input is an array of numbers 0 thru to 9. Here, an "Increasing Value Part Array" means
a part of an array in which successive numbers are increasing.

For example, "12", "49" and "678" are all "Increasing Value Part Arrays" but "53" and "22" are not.

Given Above, implement a program to return the longest "Increasing Value Part Array" for any array
input. e.g. "134297381"
"""


def long_inc_part_arr(sequence):
    length = len(sequence)
    longest_arr = []
    inter_arr = [sequence[0]]
    for i in range(length - 1):
        if sequence[i] < sequence[i+1]:
            inter_arr.append(sequence[i + 1])
        else:
            inter_arr = [sequence[i + 1]]
        if len(longest_arr) < len(inter_arr):
            longest_arr = inter_arr

    return longest_arr


if __name__ == '__main__':
    sequence = "134297381"
    print (long_inc_part_arr(sequence))
