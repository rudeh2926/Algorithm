n = int(input())
a = input()
b = list(reversed(a))

while 1 :
    if b.count('s') == b.count('t') : 
        break
    else :
        b.pop(-1)

b.reverse() 
print(''.join(b))
