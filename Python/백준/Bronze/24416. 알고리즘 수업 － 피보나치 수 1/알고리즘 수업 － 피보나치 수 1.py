def fib(n):
    a = [0] * (n + 1)
    a[1] = a[2] = 1
    for i in range(3, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]

def fibonacci(n):
    return n - 2

n = int(input())
print(fib(n), fibonacci(n))