a, b, n=map(int, input().split())
if(a==1 and b==1):
    print(1)
    exit(0)
def gcd(a,b):
    if(b != 0):
        return gcd(b, a%b)
    else:
        return a
i=0
while(1):
    if(i%2==0):
        s=gcd(a,n)
        n=n-s
    else:
        s=gcd(b,n)
        n=n-s
    i+=1
    if(n==0):
        break
if(i%2==0):
    print(1)
else:
    print(0)