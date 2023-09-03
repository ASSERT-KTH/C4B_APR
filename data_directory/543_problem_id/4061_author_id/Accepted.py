n=int(input())
a=0
c=0
while a*1234567<=n :
    b=0
    v=a*1234567
    while a*1234567+b*123456<=n :
        if (n-v-b*123456)%1234==0 :
            print('YES')
            c=1
            break
        b=b+1
    a=a+1
    if c==1 :
        break
if c==0 :
    print('NO')
l=0