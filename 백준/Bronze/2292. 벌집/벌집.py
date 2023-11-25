n = int(input())

a, b = 1, 1
while n > a:
    a += 6 * b
    b += 1

print(b)