s=list(input())
ans=0
i=1
while i<len(s):
    if (s[i]=='K')and(s[i-1]=='V'):
        ans+=1
        i+=2
    else:i+=1
i=2
while i<len(s):
    if ((s[i]=='K')and(s[i-1]=='K')and(s[i-2]!='V'))or((s[i]=='V')and(s[i-1]=='V')and(s[i+1]!='K')):
        ans+=1
        break
    else:i+=1
print(ans)