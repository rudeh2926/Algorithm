candy = int(input())
result = 0
for a in range(candy):
    for b in range(candy):
        for c in range(candy):
            if a + b + c == candy:
                if b >= c + 2:
                    if a != 0 and b != 0 and c != 0:
                        if a % 2 == 0:
                            result += 1
print(result)