a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
c = sorted(b)
for i in range(len(b)):
    print(c[i])