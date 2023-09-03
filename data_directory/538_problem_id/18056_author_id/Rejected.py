def cnt(s,v):
    ans=0
    for i in s:
        if i==v:
            ans+=1
    return ans


s=[int(z) for z in input().split()]
mx=0
for i in range(1000):
    mx=max(mx,max(cnt(s,i),3)*i)
print(sum(s)-mx)