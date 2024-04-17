def solution(nums):
    z = ''
    a = len(nums)//2
    b = set(nums)
    c = list(b)
    d = len(c)

    if a < d:
        z = a
    else:
        z = d
    return z