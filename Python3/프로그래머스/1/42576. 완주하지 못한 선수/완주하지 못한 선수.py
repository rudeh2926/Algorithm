def solution(participant, completion):
    a = {}
    b = 0
    for i in participant:
        a[hash(i)] = i
        b += hash(i)

    for j in completion:
        b -= hash(j)

    return a[b] 