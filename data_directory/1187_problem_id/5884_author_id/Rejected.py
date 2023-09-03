a=str(input(""))
length=len(a)

count=0
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
    b=a.lower()
    b=b.capitalize()
    print(b)