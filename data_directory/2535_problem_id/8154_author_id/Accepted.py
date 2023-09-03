n,m=map(int,input().split())
sum=0
for i in range (1,n+1):sum+=i
m=m%sum
for i in range (1,n+1):
    m-=i
    if m<0:
        m+=i
        break
print (m)