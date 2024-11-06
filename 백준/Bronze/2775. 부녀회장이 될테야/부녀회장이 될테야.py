t = int(input())
for _ in range(t):
    floor = int(input())  # 층 수
    num = int(input())  # 호 수
    f0 = [x for x in range(1, num + 1)]  # 0층: 1부터 num까지의 호실 값

    for i in range(floor):  # 각 층에 대해 반복
        for j in range(1, num):
            f0[j] += f0[j - 1]  # 이전 호실 사람 수를 더함
    print(f0[num-1])  # 마지막 호실의 사람 수 출력