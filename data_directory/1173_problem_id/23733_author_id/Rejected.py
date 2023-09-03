def find(x,b):
    ans=0
    while x>0:
        ans+=x%b
        x//=b
    return ans

sum=0
t=int(input())
for i in range(2,t):
    sum+=find(t,i)
print(sum,t-2,sep="/")