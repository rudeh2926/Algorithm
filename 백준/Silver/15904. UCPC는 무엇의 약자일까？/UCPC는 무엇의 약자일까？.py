a = input()
b = ['U', 'C', 'P', 'C']
c = 0
for d in b:
    if d in a:
        c += 1
        a = a[a.index(d) + 1:]
    else:
        print('I hate UCPC')
        break
if c == 4:
    print('I love UCPC')