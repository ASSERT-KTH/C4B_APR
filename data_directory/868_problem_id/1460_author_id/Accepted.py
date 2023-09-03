a=int(input())
if a==0:
    print(1)
    exit(0)
a%=4
if a==0:
    print(6)
elif a==1:
    print(8)
elif a==2:
    print(4)
elif a==3:
    print(2)