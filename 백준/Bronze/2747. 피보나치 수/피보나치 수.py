n = int(input())
nList = [-1] * (n+1)
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if nList[n] != -1:
        return nList[n]
    nList[n] = fibo(n - 1) + fibo(n - 2)
    return nList[n]

print(fibo(n))