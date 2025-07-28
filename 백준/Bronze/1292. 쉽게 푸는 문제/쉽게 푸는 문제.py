n, m = map(int, input().split())
data = [0]
result = 0
for i in range(1, m+1):
    for j in range(i):
        data.append(i)

for i in range(n, m+1):
    result += data[i]
print(result)