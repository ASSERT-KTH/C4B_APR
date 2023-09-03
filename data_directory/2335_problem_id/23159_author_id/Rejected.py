s=['h','e','l','l','o']
a=input()
c=[]
for i in range(len(a)):
    if a[i] in s:
        c.append(a[i])
x=1
while True:
    if c[0]!='h':
        c.pop(0)
    else:
        break
d=1
while True:
    if len(c)<5:
        break
    if c[d]!=s[x]:
        c.pop(d)
    else:
        x+=1
        d+=1
    if (d==len(c)) or (x==len(s)):
        break
if (''.join(c))[:5]=='hello':
    print('YES')
else:
    print('NO')