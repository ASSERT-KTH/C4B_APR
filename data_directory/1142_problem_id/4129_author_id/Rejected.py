n,a,b=map(int,input().split())
n-=a
if n>b and b-n>0:
    print(b)
else:
    print(n)