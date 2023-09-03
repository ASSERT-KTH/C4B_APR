def kasra(a):
    m=0
    a=0
    while a!=0:
        y=a%10
        a=a//10
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