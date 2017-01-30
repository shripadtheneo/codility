"""
Write a function:

def solution(A)
that, given a non-empty zero-indexed array A of N integers, returns the minimal positive integer (greater than 0) that
does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [-2147483648..2147483647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
arguments).
Elements of input arrays can be modified.
"""


def solution(A):
    arraydict = {}

    for number in A:
        if number in arraydict:
            arraydict[number] += 1
        else:
            arraydict[number] = 1

    for expected_missing in range(1, len(A) + 2):
        if expected_missing in arraydict:
            continue
        else:
            return expected_missing

    return -1

if __name__ == '__main__':
    print "Please enter the array: "
    A = raw_input()
    A = map(int, A.split())
    print solution(A)
