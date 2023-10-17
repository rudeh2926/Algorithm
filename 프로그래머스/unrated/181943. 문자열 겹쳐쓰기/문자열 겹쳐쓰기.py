def solution(my_string, overwrite_string, s):
    answer = ''
    if len(my_string[s:]) > len(overwrite_string):
        answer = my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]
    else:
        answer = my_string[0:s] + overwrite_string
    
    return answer