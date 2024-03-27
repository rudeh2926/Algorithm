a = int(input())

s = list(map(int, input().split()))

st = []

b = 1
for student in s:
    st.append(student)
    while st and st[-1] == b:
        st.pop()  
        b += 1  

if st:
    print('Sad')
else:
    print('Nice')