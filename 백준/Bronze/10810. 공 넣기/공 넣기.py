a, b = map(int, input().split())
ba = [0] * (a+1)

for _ in range(b):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        ba[n] = k 

for i in range(1, a+1):
    print(ba[i], end = ' ')