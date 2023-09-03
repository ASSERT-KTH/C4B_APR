s=input()
i=0
f=1
while f<7 and i<len(s)-1:
    if s[i]==s[i+1]:
        f+=1
    else:
        f=0
    i+=1
a='YES' if f==7 else 'NO'
print(a)