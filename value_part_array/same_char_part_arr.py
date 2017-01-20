"""
Assume the input is an array of alphabets, both capital and small, A thru to Z and a thru to z.
Here, a "Same Character Part Array" means a part of an array in which successive characters are
same(case sensitive).

For example, "aa", "AA", "bb" and "BB" are all "Same Character Part Arrays" but "aA" "ab" and
"Ab" are not.

Given Above, implement a program to return the longest "Same Character Part Array" for any array
input. e.g. "AaBBBcC"
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
    sequence = "AaBBBcC"
    print (long_same_part_arr(sequence))
