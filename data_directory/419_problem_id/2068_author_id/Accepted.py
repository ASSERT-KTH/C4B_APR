n,a,b=map(int,input().split())
if(b>0):
    b=round(b%n)
    if(a+b>n):
        print(a+b-n)
    else:
        print(a+b)
elif(b==0):
    print(a)
else:
    b=round(abs(b)%n)
    if(b-a<0):
        print(a-b)
    elif(a-b==0):
        print(n)
    else:
        print(n-(b-a))