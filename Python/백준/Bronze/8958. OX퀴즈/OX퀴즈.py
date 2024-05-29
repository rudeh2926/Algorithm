a = int(input())
for _ in range(a):
    ox = list(input())
    b = 0
    s = 0 
    for i in ox:
        if i == 'O':
            b += 1  
            s += b 
        else:
            b = 0
    print(s)