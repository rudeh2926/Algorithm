a = list(map(int, input().split()))

if a == sorted(a, reverse=False):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')