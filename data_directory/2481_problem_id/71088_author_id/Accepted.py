import math
x=int(input())
n= int(math.log(((x/5)+1),2))
size=int(math.pow(2,n))
rem=x-5*(size-1)-1
p=rem//size
if  p==0:
    print("Sheldon")
elif p==1:
    print("Leonard")
elif p==2:
    print("Penny")
elif p==3:
    print("Rajesh")
else:
    print("Howard")