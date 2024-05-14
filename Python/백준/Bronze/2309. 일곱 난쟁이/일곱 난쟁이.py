from itertools import combinations

# 9번 반복하여 9개의 정수를 a 리스트에 저장
a = [int(input()) for _ in range(9)]

# a에서 7개의 원소를 뽑아 가능한 모든 조합을 생성
#  생성된 조합을 b에 하나씩 대입하여 반복문을 수행
for b in combinations(a, 7):
    if sum(b) == 100:
        # 정렬된 조합의 각 숫자를 하나씩 num에 대입하여 반복문을 수행
        for num in sorted(b):
            print(num)
        break
