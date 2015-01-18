import string

def solution(V, R):
    # V in radix R is V % R in reversed order
    #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    alphabet = string.digits + string.letters
    divresult = abs(V)
    expresult = ''
    while divresult != 0:
        divresult, remainder = divmod(divresult, R)
        expresult = alphabet[remainder] + expresult
    if V < 0:
        return '-' + expresult
    else:
        return expresult
