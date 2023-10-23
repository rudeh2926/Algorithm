import sys

a = int(sys.stdin.readline())
b = []

for i in range(a):
    b.append(sys.stdin.readline().strip())
c = set(b)
b = list(c)
b.sort()
b.sort(key=len)

for i in b:
    print(i)