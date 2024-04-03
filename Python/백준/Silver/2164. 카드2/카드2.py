from collections import deque

a = int(input())
b = deque([i for i in range(1, a + 1)])

while (len(b) > 1):
    b.popleft()
    c = b.popleft()
    b.append(c)

print(b[0])