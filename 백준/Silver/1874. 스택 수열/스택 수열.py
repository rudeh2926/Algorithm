count = 1
t = True
stack = []
a = []

b = int(input())
for i in range(b):
    n = int(input())
    while count <= n:
        stack.append(count)
        a.append('+')
        count += 1

    if stack[-1] == n:
        stack.pop()
        a.append('-')
    else:
        t = False
        break

if t == False:
    print("NO")
else:
    for i in a:
        print(i)