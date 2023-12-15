import sys
a = int(sys.stdin.readline())
s=[]
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    s.append([b, c])
s.sort()
for i in s:
    print(i[0], i[1])