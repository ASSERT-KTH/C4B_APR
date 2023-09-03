n,a,b=map(int,input().split())
if(n==1):
    print(1)
else:
    if(a==1 and b==-1):
        print(n)
    elif(a==n and b==1):
        print(1)
    elif(abs(b)==n):
        print(a)
    elif(b>0):
        if(b>n):
            b=round(b%n)
            if(a+b>n):
                print(abs(a+b-n))
            else:
                print(abs(a+b))
        else:
            if(a+b>n):
                print(abs(a+b-n))
            else:
                print(abs(a+b))
    else:
        if(abs(b)>n):
            b=round(abs(b)%n)
            if(a+b>n):
                print(abs(a+b-n))
            else:
                print(abs(a+b))
        else:
            if(a+b>n):
                print(abs(a+b-n))
            else:
                print(abs(a+b))