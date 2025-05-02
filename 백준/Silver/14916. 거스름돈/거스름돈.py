money = int(input())
result = 0
while True:
    if money % 5 == 0:
        result += money//5
        break
    else:
        money -= 2
        result += 1
    if money <= 0:
        break
if money < 0 or money == 1:
    print(-1)
else:
    print(result)