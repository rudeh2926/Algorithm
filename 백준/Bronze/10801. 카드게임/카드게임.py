a = list(map(int, input().split()))
b = list(map(int, input().split()))
ac, bc = 0, 0
for i in range(10):
    if a[i] > b[i]:
        ac += 1
    elif a[i] < b[i]:
        bc += 1

if ac > bc:
    print('A')
elif bc > ac:
    print('B')
else:
    print('D')