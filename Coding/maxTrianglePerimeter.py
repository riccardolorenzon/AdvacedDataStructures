def solution(A):
    #i can sort the array becouse the order of P, Q, R is relative and not absolute
    A.sort()
    n= len(A)
    #once the array is sorted i can valuate only the first contion becouse the other 2
    #are implicitly verified
    #max perimeter
    max_perimeter = -1
    for i in xrange(1, n-1):
        if(A[i-1] + A[i] > A[i+1]):
            perimeter = A[i-1] + A[i] + A[i+1]
            if perimeter >= max_perimeter:
                max_perimeter = perimeter
    return max_perimeter
