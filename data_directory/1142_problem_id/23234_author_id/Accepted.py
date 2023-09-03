n,a,b = map(int,input().split())
ans =n-a
if ans>b+1:
    ans=b+1
print(ans)