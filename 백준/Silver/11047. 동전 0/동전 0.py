a, b = map(int, input().split())
m = []
for i in range(a):
    m.append(int(input()))
m = sorted(m, reverse=True)

c = 0
for i in m:
    if b==0:
      break
    c += b//i
    b %= i

print(c)