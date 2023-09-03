q,w,e=map(int,input().split())
a=w-q
if q==w:
    print ('YES')
elif a*e>=0:
    if a%e==0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')