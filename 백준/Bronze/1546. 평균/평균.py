a = int(input())
m = list(map(int, input().split()))
mx = max(m)

for i in range(a):
    m[i] = m[i] / mx * 100
print("%.2f" % (sum(m) / a))