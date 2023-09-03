m=int(input())
if(m==1):
    print("1")
elif(m==2):
    print("2")
elif(m%2==0):
    
    print((m-1)*(m-2)*(m-3))


else:
    print(m*(m-1)*(m-2))