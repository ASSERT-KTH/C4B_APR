n=int(input())
if(n%4 and n%2==0):
    print(int(n/4))
elif(n%2==0):
    print(int(n/4)-1)
else:
    print(0)