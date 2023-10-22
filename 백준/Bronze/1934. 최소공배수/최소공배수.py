import math
a = int(input())
for _ in range(a):
    b, c = map(int, input().split())
    print(math.lcm(b,c))