#Allah is the most gracious and the Most Marchiful
m=int(input())
if(m==1):
    print("1")
elif(m==2):
    print("2")
elif(m%2==0):
    if(m%3==0):
        ans=(m-1)*(m-2)*(m-3)
    else:
        ans=(m)*(m-1)*(m-3)


    print(round(ans))
else:
    print(m*(m-1)*(m-2))