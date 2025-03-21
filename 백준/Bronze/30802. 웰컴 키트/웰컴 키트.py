N = int(input())
sizes = map(int, input().split())
T, P = map(int, input().split())

cnt = 0
for size in sizes:
    if size == 0: 
        continue
    elif size % T == 0:
        cnt += size // T
    else:
        cnt += size // T + 1

print(cnt)
print(N//P, N%P)