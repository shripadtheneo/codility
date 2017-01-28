def solution(A):
    current = 0
    length = len(A)
    forward = A[0]
    backward = sum(A[1:])
    minimum = abs(forward - backward)

    for i in range(1, length - 1):
        forward += A[i]
        backward -= A[i]
        current = abs(forward - backward)
        if current < minimum:
            minimum = current

    return minimum

if __name__ == '__main__':
    print "Please enter the array: "
    A = raw_input()
    A = map(int, A.split())
    print solution(A)
