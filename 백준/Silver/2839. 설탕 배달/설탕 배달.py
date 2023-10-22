a = int(input())
c = 0
while a >= 0:
    if a % 5 == 0:
        c += int(a // 5)
        print(c)
        break
    a -= 3
    c += 1
else:
    print(-1)