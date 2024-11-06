num = int(input()) # 28
n = num
cnt: int = 0
while True:
    a = num // 10 #2
    b = num % 10 #6
    c = (a + b) % 10 #6 "8"
    num = (b * 10) + c
    cnt = cnt + 1
    if n == num:
        break

print(cnt)