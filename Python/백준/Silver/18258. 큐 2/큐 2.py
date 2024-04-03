from collections import deque
import sys

n = int(sys.stdin.readline().strip())
b = deque()

for i in range(n):
    a = sys.stdin.readline().strip().split()
    c = lambda x: print(x)
    if a[0] == 'push':
        b.append(a[1])
    elif a[0] == 'pop':
        c(b.popleft() if b else -1)
    elif a[0] == 'size':
        c(len(b))
    elif a[0] == 'empty':
        c(1 if not b else 0)
    elif a[0] == 'front':
        c(b[0] if b else -1)
    elif a[0] == 'back':
        c(b[-1] if b else -1)
