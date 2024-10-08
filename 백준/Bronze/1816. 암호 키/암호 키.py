for _ in range(int(input())):
    num = int(input())
    for s in range(2, 1000001):
        if num % s == 0:
            print('NO')
            break
        if s == 1000000:
            print('YES')