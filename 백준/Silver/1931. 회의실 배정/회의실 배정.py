def a(n, b):
    b.sort(key=lambda x: (x[1], x[0]))
    c = 0
    last = 0
    
    for start, end in b:
        if start >= last: 
            c += 1
            last = end 
    
    return c

n = int(input())
m = []

for _ in range(n):
    start, end = map(int, input().split())
    m.append((start, end))

print(a(n, m))
