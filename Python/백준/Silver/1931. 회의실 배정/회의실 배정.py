a = int(input())
b = []
for i in range(a):
    c, d = map(int, input().split())
    b.append((c, d))
b.sort(key=lambda e: (e[1], e[0]))
w = 0
ct = 0
for c, d in b:
    if c >= w:
        w = d
        ct += 1
print(ct)