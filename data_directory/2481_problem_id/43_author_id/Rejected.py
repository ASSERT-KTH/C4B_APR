n = int(input())

c=1
while(c*5<n):
    n-=c*5
    print("n ",n)
    c*=2
    print("C ",c)

if((n-1)/c==0):
    print("Sheldon")
if((n-1)/c==1):
    print("Leonard")
if((n-1)/c==2):
    print("Penny")
if((n-1)/c==3):
    print("Rajesh")
if((n-1)/c==4):
    print("Howard")