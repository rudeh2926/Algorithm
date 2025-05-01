sti = []
for _ in range(5):
    a = input()
    sti.append(a)

for j in range(15):
    for i in range(5):
        if j < len(sti[i]):
             print(sti[i][j], end='')