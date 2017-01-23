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
    print "Please input the array: "
    sequence = raw_input()
    print (long_same_part_arr(sequence))

"""
Note:
    This program is solved using the Dynamic Programming approach. First concentration was on the
    time complexity so need to traverse the loop only once causing us to make sure that we keep the
    result stored in my first python function which is commented out. Result was time
    complexity to be O(n). (Since there is only once looping through the sequence as well as other have
    constant time so time complexity is O(n)). Then there was need of reducing the space complexity so
    rather than using two list, 2 array of size just 2 are used reducing the space complexity too.

    Now for how i used the reusability and extendability is that for last 2 questions, code is same and
    haven't changed at all while only the condition is changed between first part of code and second part
    of code. As python is not strictly typed language it is possible in python but to do it in Java i
    will need to make use of character array with type casting at the time of condition checking.
    (Will code that later)
"""