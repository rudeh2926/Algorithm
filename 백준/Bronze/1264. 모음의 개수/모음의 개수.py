while True:
    s = input()
    if s == '#':
        break
    c = 0
    for i in s:
        if i in 'aeiouAEIOU':
            c += 1
    print(c)