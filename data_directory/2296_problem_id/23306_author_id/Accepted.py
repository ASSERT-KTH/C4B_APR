m,n=map(int,input().split(" "))
if(m%2==0):
    print((m//2)*(n))
else:
    suma=(m//2)*(n)
    c=n
    d=1
    suma+=((c//2)*(d))
    print(suma)