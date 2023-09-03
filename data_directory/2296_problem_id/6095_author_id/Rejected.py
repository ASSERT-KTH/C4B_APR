m,n=map(int,input().split(' '))
if n==1 or m==1:
    if n==1:
        print(m//2)
    elif m==1:
        print(n//2)
elif (m%2!=0) and (n%2!=0):
    if m>n:
        e=m
        r=n
    else:
        e=n
        r=m
    u=e-1
    b=(u*r)//2
    v=e//2
    print(b+v)
else :
    fuck=(m*n)//2
    print (fuck)