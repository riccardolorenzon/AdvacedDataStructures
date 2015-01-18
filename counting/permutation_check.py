"""
Check whether array A is a permutation.
"""
def solution(A):
    n = len(A)
    #each array keeps occurences of values(max = min = 1)
    occurences = [0] * n
    for i in xrange(0,n):
        #check if the value is bigger than n
        if (A[i] > n):
            return 0
        # values starts from 1 while the array is 0-indexed
        pos = A[i] - 1
        if (occurences[pos] == 0):
            occurences[pos] = 1
        else:
            #element occurs twice in A => no permutation
            return 0
    result = 1
    for i in xrange(0,n):
        result = result and occurences[i]
    return result