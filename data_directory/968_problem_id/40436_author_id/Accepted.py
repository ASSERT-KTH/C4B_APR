a = [int(i) for i in input().split()]
m = int(a[0])
d = int(a[1])

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if d<=5:
        print("5")
    else:
        print("6")
if m==2:
    if d==1:
        print("4")
    else:
        print("5")
if m==4 or m==6 or m==9 or m==11:
    if d<=6:
        print("5")
    else:
        print("6")