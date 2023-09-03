a,b=map(int,input().split())
count=0
for i in range(a,b+1):
    c=str(bin(i))[2:]
    k=c.count('0')
    if k==1:
        count+=1
print(count)