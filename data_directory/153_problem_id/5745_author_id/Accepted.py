n=int(input())
if(n%2==1):
    print(0)
else:
    m=n//2
    if(m%2==0):
        m-=1
    print(m//2)