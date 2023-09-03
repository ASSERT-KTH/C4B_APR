def kasra(n):
    m=0
    a=0
    while n!=0:
        y=n%10
        n=n//10
        if y!=0:
            m=m*10+y
    while m!=0:
        t=m%10
        m=m//10
        a=a*10+t
    return a
a=int(input())
b=int(input())
if kasra(a+b)==kasra(a)+kasra(b):
    print('YES')
else:
    print('NO')