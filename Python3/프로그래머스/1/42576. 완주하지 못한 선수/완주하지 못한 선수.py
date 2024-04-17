def solution(participant, completion):
    a = 0
    b = {}

    for c in participant:
        a += hash(c)
        if c in b: # 동명이인이 있다면 +1 함
            b[c] += 1
        else: # 아니면 그냥 1 추가
            b[c] = 1

    for c in completion:
        a -= hash(c)
        b[c] -= 1

    for c, count in b.items():
        if count == 1:
            return c

    return None  