a = int(input())
b = {}
c = list(map(int, input().split()))
for i in c:
    if i in b:
        b[i] += 1
    else :
        b[i] = 1
e = int(input())
for i in list(map(int, input().split())):
    if i in b:
        print(b[i], end=' ')
    else:
        print(0, end=' ')