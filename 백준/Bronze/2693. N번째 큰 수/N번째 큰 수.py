data = []
n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    nList = data[i]
    nList.sort()
    print(nList[7])