"""
In a given array, find the subset of maximal sum in which the distance between consecutive elements is at most 6.
"""
def solution(A):
    n = len(A)
    # array of max M[i] K from square i
    M = [-1] * n
    i = 0
    while i != n-1:
        for j in xrange(1,7):
            if M[i] == -1 or M[i] < A[j]:
                M[i] = j
            if i + j == n-1:
                break
        i = i + M[i]

    value = A[0]
    for k in xrange(0, len(M) -1):
        value = value + A[M[k]]

    return value

