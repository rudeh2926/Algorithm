a, b = map(int, input().split())
c = 0
for i in range(1, a + 1):
    if str(i).count(str(b)) > 0:
        if i > 9:
            c += list(str(i)).count(str(b))
        else:
            c += 1

print(c)