n,a,b,c=[int(i) for i in input().split()]
dp=(n+1)*[-n-1]
l=[a,b,c]
dp[0]=0
l.sort()
for i in range(l[0],l[1]):
    if i%l[0]==0:
        dp[i]=i//l[0]
for i in range(l[1],l[2]):
    p=[]
    if dp[i-l[0]]!=-n-1:
        p.append(dp[i-l[0]]+1)
    if dp[i-l[1]]!=-n-1:
        p.append(dp[i-l[1]]+1)
    if len(p)>0 and max(p)>dp[i]:
        dp[i]=max(p)
    
for i in range(l[2],n+1):
    p=[]
    if i>=a and dp[i-a]!=-n-1:
        p.append(dp[i-a]+1)
    if i>=b and dp[i-b]!=-n-1:
        p.append(dp[i-b]+1)
    if i>=c and dp[i-c]!=-n-1:
        p.append(dp[i-c]+1)
    if len(p)>0 and max(p)>dp[i]:
        dp[i]=max(p)
if dp[n]==n+1:
    print(-1)
else:
    print(dp[n])