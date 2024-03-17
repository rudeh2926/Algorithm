def solution(num_list):
    a = 0
    if len(num_list) >= 11:
        for i in num_list:
            a += i
    else:
        a += 1
        for i in num_list:
            a *= i
    return a