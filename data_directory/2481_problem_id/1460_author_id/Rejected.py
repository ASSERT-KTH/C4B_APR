x=int(input())
y=5
z=1
while x>y*z:
    x-=y*z
    z+=1

if x-z*1<1:
    print("Sheldon")
elif x-z*2<1:
    print("Leonard")
elif x-z*3<1:
    print("Penny")
elif x-z*4<1:
    print("Rajesh")
elif x-z*5<1:
    print("Howard")