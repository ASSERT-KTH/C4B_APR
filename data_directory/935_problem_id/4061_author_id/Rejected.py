n=int(input())
def ARG(n) :
    for i in range(2,n+1) :
        if (n+1)%i==0 :
            return 1
    return 2
if ARG(n)==2 :
    if n==1 :
        print(3)
    else :
        print(2)
else :
    print(1)