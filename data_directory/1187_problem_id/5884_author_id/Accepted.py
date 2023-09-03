a=str(input(""))
length=len(a)

count=0
check1=0
#print(a[0].islower())
if(a[0].islower()==True):
    count=1

for i in range(length):
    if a[i].isupper()==True:
        count=1
 #       print(a[i].isupper(),i)
    else:
        if(a[i].islower()==True and i!=0):
            count=2
            print(a)
            exit()
if count==2:
    print(a)
elif count==1:
    
    for i in range(length):
        if a[i].isupper()==True:
            check1=check1+1
    if check1==length:
        b=a.lower()
        print(b)
    else:
        b=a.lower()
        b=b.capitalize()
        print(b)