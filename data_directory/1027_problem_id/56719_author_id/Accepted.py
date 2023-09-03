a=int(input())
if(a==10):
    print(0,end="\n")
elif(a>21 or a<10):
    print(0)
else:
    a=a%10
    if(a==0):
        print(15)
    else:
        print(4)