n=int(input())
a=n//7
if n%7==0:
    print(a*2,a*2)
else:
    if n%7==1:
        print(a*2,a*2+1)
    elif 6>n%7>=2:
        print(a*2,a*2+2)
    elif n%7==6:
        print(a*2+1,a*2+2)