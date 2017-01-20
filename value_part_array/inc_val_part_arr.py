"""
Assume the input is an array of numbers 0 thru to 9. Here, an "Increasing Value Part Array" means
a part of an array in which successive numbers are increasing.

For example, "12", "49" and "678" are all "Increasing Value Part Arrays" but "53" and "22" are not.

Given Above, implement a program to return the longest "Increasing Value Part Array" for any array
input. e.g. "134297381"
"""


def long_inc_part_arr(A):
    length = len(A)
    final_arr = []
    inter_arr = [str(A[0])]
    for i in range(length - 1):
        if A[i] < A[i+1]:
            inter_arr.append(str(A[i+1]))
        else:
            inter_arr = [str(A[i + 1])]
        if len(final_arr) < len(inter_arr):
            final_arr = inter_arr

    return final_arr


if __name__ == '__main__':
    A = [1, 7, 4, 2, 9, 1, 3, 8, 9]
    print (long_inc_part_arr(A))
