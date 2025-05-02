weight = int(input())
result = 0
while weight >= 0:
    if weight % 5 == 0:
        result += weight // 5
        print(result)
        break
    else:
        weight -= 3
        result += 1
else:
    print(-1)