result = []
a = 0
for _ in range(5):
    result.append(int(input()))
result.sort()
print(sum(result) // 5)
print(result[2])