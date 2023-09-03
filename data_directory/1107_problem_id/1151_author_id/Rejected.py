def nod(a,b):
    maxnod=-1
    if a<b:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                maxnod=i
    else:
        for i in range(1,b+1):
            if a%i==0 and b%i==0:
                maxnod=i
    return(maxnod)
a,b,n=map(int,input().split())
c=0
while n>=0:
    c+=1
    n-=nod(a,b)
if c%2==0:
    print(0)
else:
    print(1)