def fill_map(A, S, col_num, row_num, numb, prov):

    #check if the square A[i][j] has one of its neighbour with the same value,
    #   if this is verified =>
    #       fill 1 on S[i][j] and recurively call itself passing its neighbour parameters
    #   else => return
    # rows number
    N = len(A)
    # cols number
    M = len(A[0])
    if col_num < 0 or col_num > M - 1 or row_num < 0 or row_num > N -1 or A[row_num][col_num] != numb:
        return
    else:
        S[row_num][col_num] = 1
        if prov != 2:
            #N
            if row_num > 0:
                fill_map(A,S,col_num, row_num -1, numb, 0)
        if prov != 3:
            #E
            if col_num < M - 1:
                fill_map(A,S,col_num+1, row_num, numb, 1)
        if prov !=  0:
            #S
            if row_num < N -1:
                fill_map(A, S, col_num, row_num+1, numb, 2)
        if prov != 1:
            #W
            if col_num > 0:
                fill_map(A,S,col_num -1, row_num, numb, 3)


# find number of adjacent squares
def solution(A):
    # rows number
    N = len(A)
    # cols number
    M = len(A[0])
    # support matrix
    S = [[0] * M for x in xrange(0, N)]
    total_countries = 0
    for i in xrange(0, N):
        for j in xrange(0,M):
            if S[i][j] == 1:
                pass
            else:
                total_countries += 1
                fill_map(A, S, j, i, A[i][j], -1);

    return total_countries

A = [[5,4,4], [4,3,4], [3,2,4], [2,2,2], [3,3,4], [1,4,4], [4,1,1]]
print solution(A)

# output is 11