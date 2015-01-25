
def get_prefix_array(A):
    n = len(A)
    S = A[::-1]
    last_value = 0
    for i in xrange(0, n):
        S[i] += last_value
        last_value = S[i]
    return S

def solution(A):

    n = len(A)
    if n == 0:
        return -1

    eq_index = -1
    partial_sum = 0
    S = get_prefix_array(A)

    for i in xrange(0, n):
        partial_sum += A[i]
        if partial_sum == S[n-i-3]:
            eq_index = i+1
            return eq_index
    return eq_index