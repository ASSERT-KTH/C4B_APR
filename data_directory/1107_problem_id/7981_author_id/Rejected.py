a,b,n=list(map(int,input().split()))
def gcd(x,y):
    while(x!=y):
        x,y=max(x,y),min(x,y)
        x-=y
    return y
x=gcd(a,b)
print((n//x+1)%2)