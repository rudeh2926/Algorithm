a = int(input())
for _ in range(a):
    b, c = input().split()
    for i in c:
        print(i * int(b), end='')
    print()