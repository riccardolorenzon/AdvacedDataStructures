
#max adjacency after coin flipping
def solution(A):
    n = len(A)
    if n == 0 or n == 1:
        #case empty or single element array
        return 0

    max_score = -1
    changed_coin = -1
    total_adj = 0
    for i in xrange(0,n):
        if i == 0:
            if A[i+1] == A[i]:
                total_adj += 1
        if i == n-1:
            pass
        if i != 0 and i != n-1:
            if A[i+1] == A[i]:
                total_adj += 1

    for i in xrange(0,n):
        score = 0

        if A[i] == 0:
            changed_coin = 1
        else:
            changed_coin = 0
        #foreach index a 'score' is calculated
        #   if takes part of 1 adj => score -1
        #   if takes part of 2 adj => score -2
        #   if after changing it would take part of 1 adj => score +1
        #   if after changing it would take part of 2 adj => score +2
        #   if index has a score bigger than max value => assign to max_index_to_max_adj
        if i == 0:
            if A[i+1] == A[i]:
                score -= 1
            if A[i+1] == changed_coin:
                score += 1
            if score >= max_score:
                max_score = score
        if i == n-1:
            if A[i-1] == A[i]:
                score -= 1
            if A[i-1] == changed_coin:
                score += 1
            if score >= max_score:
                max_score = score
        if i != 0 and i != n-1:
            if A[i+1] == A[i]:
                score -= 1
            if A[i-1] == A[i]:
                score -= 1
            if A[i+1] == changed_coin:
                score += 1
            if A[i-1] == changed_coin:
                score += 1
            if score >= max_score:
                max_score = score
    return total_adj + max_score