a = int(input())

stack = []

for _ in range(a) :
    N = int(input())
    if N == 0 :
        stack.pop()
    else :
        stack.append(N)

print(sum(stack))