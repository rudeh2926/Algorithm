a = int(input()) 
b = list(map(int, input().split()))  

b.sort() 
c = 0 

for i in range(1, a+1):
    c += sum(b[0:i])  
print(c)