a=int(input()) 
b=[0]*(a+1) 
for i in range(2,a+1):
    b[i]=b[i-1]+1 
    if i%2==0: 
        b[i]=min(b[i],b[i//2]+1)
    if i%3==0: 
        b[i]=min(b[i],b[i//3]+1)
print(b[a])