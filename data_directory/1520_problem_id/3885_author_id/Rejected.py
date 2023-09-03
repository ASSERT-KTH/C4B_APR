[n,a,b,c]=[int(x) for x in input().split()]
dp=[0 for x in range(n+1)]
dp[a]=1
dp[b]=1
dp[c]=1
for i in range(n+1):
    if i>=a and dp[i-a]>0:
        dp[i]=max(dp[i],dp[i-a]+1)
    if i>=b and dp[i-b]>0:
        dp[i]=max(dp[i],dp[i-b]+1)
    if i>=c and dp[i-c]>0:
        dp[i]=max(dp[i],dp[i-c]+1)
print(dp[n])