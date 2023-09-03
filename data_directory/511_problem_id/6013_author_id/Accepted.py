a,b,c=map(int,input().split(' '))
if(c==0): 
    if(b==a):
        print('YES')
    else:
        print('NO')
elif((b-a)%c==0 and (c>0 and a<=b or c<0 and a>=b)):
    print('YES')
else:
    print('NO')