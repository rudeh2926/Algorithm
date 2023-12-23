a = int(input())

b = 0
for i in range(1, a+1):
    c = list(map(int, str(i)))
    if i < 100:
        b += 1  
    elif c[0]-c[1] == c[1]-c[2]:
        b += 1  
print(b)