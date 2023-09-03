import sys,math

s=list(map(int, input().split()))
n=s[0]
k=s[1]
t=s[2]

ans = [0 for i in range(n+1)]
d = math.floor(t*n*k/100)

for i in range ((d//k)):
    ans[i]=k
ans[(d//k)]=d%k
s=""
for i in range(n):
    s=s+str(ans[i])+" "
print(s.strip())