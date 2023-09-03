n=int(input())
if n<13:
    print(pow(2,n))
else:
    num=pow(2,12)
    n=n-13
    ans=8092
    while n:
        ans=ans*2
        n=n-1
    print(ans)