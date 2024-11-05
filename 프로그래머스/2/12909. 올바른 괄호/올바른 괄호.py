def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack == []:
                return False
            stack.pop()
    return stack == []