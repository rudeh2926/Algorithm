def solution(n, k):
    if n >= 10:
        return (n*12000) + (k- n//10) * 2000
    return (n*12000) + (k * 2000)