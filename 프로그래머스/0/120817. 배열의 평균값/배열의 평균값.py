def solution(numbers):
    nList = map(int, numbers)
    answer = sum(nList) / len(numbers)
    return answer