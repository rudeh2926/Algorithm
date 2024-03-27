a = int(input())
for _ in range(a):
    stack = []
    b = input()
    for i in b:
        if i == '(':
            stack.append(i) 
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")