k,a,b=map(int,input().split())
if (a>=k and b>=k) or (a%k==0 and a//k!=0)  or (b%k==0 and b//k!=0):
    exit(print(a//k + b//k))
exit(print('-1'))