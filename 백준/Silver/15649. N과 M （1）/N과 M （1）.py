def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
    for i in range(1, n+1):
        if visited[i]:
            continue
        else:
            visited[i] = True
            s.append(i)
            dfs()
            visited[i] = False
            s.pop()


s = []
n, m = map(int, input().split())
visited = [False] * (n+1)

dfs()
