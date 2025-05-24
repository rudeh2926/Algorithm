n = int(input())
nList = list(map(int, input().split()))
results = [nList[0]]

for i in range(1, n):
    results.append(nList[i] * (i + 1) - sum(results))

for i in results:
    print(i, end=' ')