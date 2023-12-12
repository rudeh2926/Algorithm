a = int(input())
d = []
for i in range(a):
    c, e = map(str, input().split())
    c = int(c)
    d.append((c, e))

d.sort(key = lambda x : x[0])	

for i in d:
    print(i[0], i[1])