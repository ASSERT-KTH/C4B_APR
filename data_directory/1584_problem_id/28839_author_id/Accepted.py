s=input()
ans=s[0]
for i in range(1,len(s)):
    if s[i-1]=='/' and s[i]=='/':   continue
    ans+=s[i]
if ans[-1]=='/' and len(ans)>1: print(ans[:-1])
else:   print(ans)