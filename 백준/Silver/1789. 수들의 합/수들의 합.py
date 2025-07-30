n = int(input())
result = 0
i = 0
while True:
    if n > i:
        i += 1
        n -= i
        result+=1
    else:
        break

print(result)