A,B,n=map(int,input().split())

if(A==0 and B==0):
    print(5)
elif(A==0):
    print("No solution")

elif((B/A)%1!=0):
    print("No solution")
else:

    v=B//A


    if(v<0):
        x=-1
    else:
        x=1
    v=pow(abs(v),1/n)
    vv=round(v)
    if(abs(vv-v)>(10**(-6))):
        print("No solution")
    else:
        print(x*int(vv))