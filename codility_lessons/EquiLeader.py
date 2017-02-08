"""
A non-empty zero-indexed array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 <= S < N - 1 and two sequences A[0], A[1], ..., A[S] and
A[S + 1], A[S + 2], ..., A[N - 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)
that, given a non-empty zero-indexed array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [-1,000,000,000..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input
arguments).
Elements of input arrays can be modified.
"""


def solution(A):
    length = len(A)
    candidate = -1
    candidate_count = 0

    for i in range(length):
        if candidate_count == 0:
            candidate = A[i]
            candidate_count += 1
        else:
            if candidate == A[i]:
                candidate_count += 1
            else:
                candidate_count -= 1

    lead_count = len([number for number in A if candidate == number])
    if lead_count <= length / 2:
        return 0
    else:
        leader = candidate

    leader_count = 0
    counter = 0
    for i in range(length):
        if A[i] == candidate:
            leader_count += 1

        if leader_count > (i + 1) / 2 and (lead_count - leader_count) > (length - i - 1) / 2:
            counter += 1
    return counter


if __name__ == '__main__':
    print "Please enter the array: "
    A = raw_input()
    A = map(int, A.split())
    print solution(A)
