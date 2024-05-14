from itertools import combinations

a = [int(input()) for _ in range(9)]

for b in combinations(a, 7):
    if sum(b) == 100:
        for num in sorted(b):
            print(num)
        break