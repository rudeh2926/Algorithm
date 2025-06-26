def dfs(start, total, plus, minus, multiply, divide):
    global maximum, minimum

    if start == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(start+ 1, total + nList[start], plus - 1, minus, multiply, divide)
    if minus:
        dfs(start+ 1, total - nList[start], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(start+ 1, total * nList[start], plus, minus, multiply - 1, divide)
    if divide:
        dfs(start+ 1, int(total / nList[start]), plus, minus, multiply, divide - 1)



n = int(input())
nList = list(map(int, input().split()))
op = list(map(int, input().split()))
maximum = -1e9
minimum = 1e9

dfs(1, nList[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)