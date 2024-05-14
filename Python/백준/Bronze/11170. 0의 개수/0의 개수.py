a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    b = 0

    for num in range(n, m + 1):
        b += str(num).count('0')

    print(b)
