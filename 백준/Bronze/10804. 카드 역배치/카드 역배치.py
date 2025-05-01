basic = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    basic[a:b+1] = basic[b:a-1:-1]

print(*basic[1:])