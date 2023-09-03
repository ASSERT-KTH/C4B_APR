n,a,b=map(int,input().split(' '))
y=a+b
while 1:
    if b==0:
        print (a)
        break
    elif y<=0:
        y+=n
    elif y>n:
        y-=n
    else :
        print (y)
        break