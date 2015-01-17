# Find the maximum number of ropes that can be attached in order, without breaking any of the ropes.
def solution(A, B, C):
    # total_weight[i] contains total weight for ith rope
    total_weight_rope = []
    total_ropes = len(C)
    rope_break = False
    i = 0
    while rope_break==False:
        # foreach node starting from the leaves i calcule the total weight ofits parent
        A[i] = A[i] - B[i] 
        if C[i] == -1:
            #root
            pass
        else:
            #to the root
            A_parent = A[C[i]]
            parent = C[i]
            heavy_child = B[i]
            while parent != -1 and rope_break == False:
                A[parent] = A[parent] - heavy_child
                #rope_break condition
                if A[parent] < 0:
                    rope_break = True
                else:
                    parent = C[parent]
        if rope_break != True:
            i+=1                 
    return i
