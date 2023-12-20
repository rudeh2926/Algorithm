def solution(n):
    a = 0
    for i in range(n+1):
        if i % 2 == 0:
            a += i
    return a