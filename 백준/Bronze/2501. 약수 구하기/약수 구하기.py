
n, m =map(int, input().split())
a = []
for i in range(1, n+1):
    if n % i == 0:
        a.append(i)
if len(a) < m:
    print(0)
else:print(a[m-1])