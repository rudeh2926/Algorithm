def solution(arr):
    a = 0 
    b = len(arr)
    while b > 1:
        b = b / 2
        a += 1
    return arr + [0] * (2 ** a - len(arr))