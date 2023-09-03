m,n=map(int,input().split(" "))
if(m%2==0):
    print((m//2)*(n))
else:
    suma=(m//2)*(n)
    a=m
    m=1
    n=a
    suma+=(n//2)*(m)
    print(suma)