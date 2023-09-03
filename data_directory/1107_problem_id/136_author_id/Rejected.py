def bmm(a,b):
    if a>b:
        z=0
        for i in range(b,0,-1):
            if a%i==0 and b%i==0:
                z=i
                break
        return z
    elif a<b:
        z=0
        for i in range(a,0,-1):
            if a%i==0 and b%i==0:
                z=i
                break
        return z
print(bmm(5,0))
a,b,n=[int(i) for i in input().split()]
z=n
f=-1
while f==-1:
    if bmm(a,z)<=z:
        z=z-bmm(a,z)
    else:
        f=1
        break
    if bmm(b,z)<=z:
        z=z-bmm(b,z)
    else:
        f=0
        break
print(f)