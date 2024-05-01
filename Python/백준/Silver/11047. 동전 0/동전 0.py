import sys
a, b = map(int, sys.stdin.readline().split())
m = []
for i in range(a):
    m.append(int(sys.stdin.readline()))
m = sorted(m, reverse=True)

c = 0
for i in m:
    if b==0:
      break
    c += b//i
    b %= i

print(c)