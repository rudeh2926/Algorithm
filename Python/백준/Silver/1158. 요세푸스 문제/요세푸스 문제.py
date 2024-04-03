a, b = map(int, input().split())
c = [i for i in range(1, a + 1)]

d = []
e = 0

for t in range(a):
    e += b - 1
    if e >= len(c):
        e = e % len(c)

    d.append(str(c.pop(e)))
print("<", ", ".join(d)[:], ">", sep='')