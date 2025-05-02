a = int(input())
person = []
for _ in range(a):
    high, weight = map(int, input().split())
    person.append([high, weight])
for i in person:
    rank = 1
    for j in person:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')