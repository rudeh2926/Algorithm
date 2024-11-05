a = []
null = []
for _ in range(1,29):
    b = int(input())
    a.append(b)


for i in range(1,31):
    if i not in a:
        null.append(i)
    else:
        continue
print(min(null))
print(max(null))