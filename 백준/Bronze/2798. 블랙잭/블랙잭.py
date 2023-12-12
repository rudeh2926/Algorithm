a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []
for i in range(a):
    for j in range(i+1, a):
        for z in range(j+1, a):
            e = c[i] + c[j] + c[z]
            if e > b:
                continue
            else:
                d.append(e)
print(max(d))