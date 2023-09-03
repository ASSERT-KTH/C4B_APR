def gcd(a, b):
    while(a!=0 and b!=0):
        if (a>b):
            a=a%b
        else:
            b=b%a
    return a+b

a, b, c=map(int, input().split(' '))
t=0
while(c>0):
    if (t==0):
        c=c-gcd(a, c)
        t=1
    else:
        c=c-gcd(b, c)
        t=0
        
if (t==1):
    if (c==0):
        print(0)
    else:
        print(1)
else:
    if (c==0):
        print(1)
    else:
        print(0)