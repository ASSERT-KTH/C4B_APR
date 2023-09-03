a=input()
#print(type(a))
c=a[0]
#print(c)
#print(type(c))
q=len(a)
f=[]
n=0
while n<q:
    e=ord(a[n])
    if e==52 or e==55:
        f.append(e)
    else:
        break

    n=n+1
#print(f)
g=len(f)
if g==q and q>1:
    print('YES')
else:
    print('NO')