import sys

a = []
for _ in range(int(sys.stdin.readline())):
    b,c,d,e = sys.stdin.readline().rstrip().split()
    c,d,e = map(int, (c, d, e))
    a.append((e, d, c, b))
a.sort()
print(a[-1][3])
print(a[0][3])