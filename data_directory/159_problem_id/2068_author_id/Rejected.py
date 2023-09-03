s=input().split()
a=list(s)
a[0]=int(a[0])
if(a[2]=="week"):
    if(a[0]>4):
        print(53)
    else:
        print(52)
else:
    if(a[0]==30):
        print(11)
    elif(a[0]==31):
        print(7)
    else:
        print(12)