"""
Find a maximal set of non((-))overlapping segments.
"""
def solution(A, B):
    segments = len(A)
    # scenario 0 segments
    if segments == 0:
        return 0
    # max non overlapping segments set size
    max_non_overlapping_segments_size = 1
    # current segment index
    current_segment = 0
    i = 1
    while i < segments:
        if B[current_segment] < A[i]:
            max_non_overlapping_segments_size +=1
            current_segment = i
        else:
            #no operations
            pass
        i += 1
    return max_non_overlapping_segments_size