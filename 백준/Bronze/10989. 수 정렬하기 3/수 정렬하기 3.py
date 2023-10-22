import sys

a = int(sys.stdin.readline())
b = [0] * 10001
for _ in range(a):
    num = int(sys.stdin.readline())
    b[num] += 1
for i in range(10001): 
    if b[i] != 0:
        for j in range(b[i]): 
            print(i)