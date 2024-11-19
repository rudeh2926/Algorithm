def solution(s):
    a=[]
    for i in s.split("},"):
        a.append(i.replace("{","").replace("}","").split(","))
    a.sort(key=len)
    answer=[]
    for i in a:
        for j in i:
            if j not in answer:
                answer.append(j)
    return list(map(int, answer))