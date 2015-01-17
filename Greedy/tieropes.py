"""
TieRopes

Tie adjacent ropes to achieve the maximum number of ropes of length >= K.
"""
def solution(K, A):
    n = len(A)
    #number of tied/not tied ropes
    j = 0
    #lenght of current rope
    length_current_rope = 0
    #total_number_ropes
    total_number_ropes = 0
    while(j < n):
        if length_current_rope + A[j] >= K:
            total_number_ropes += 1
            length_current_rope = 0
        else:
            length_current_rope += A[j]
        j+=1
    return total_number_ropes