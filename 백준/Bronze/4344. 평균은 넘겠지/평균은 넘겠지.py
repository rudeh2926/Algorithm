#입력받을 횟수 input
# list로 입력받고 index 0번째가 점수 길이 index 1부터가 점수
# 평균 구하는 공식은 index 1번부터 n번까지 점수를 다 더한 후 나누기 index 0
# 그다음은 index 1번부터 평균이 구하는 사람 카운트 한 후 백분위로 나누어 소수 3번째 자리까지 print하기
for i in range(int(input())):
    scoreList = list(map(int, input().split()))
    average = sum(scoreList[1:])/scoreList[0]
    count = 0
    for j in scoreList[1:] :
        if j > average:
            count += 1
    result = count / scoreList[0] * 100
    print("{:.3f}%".format(result))
