a=list(map(int, input().strip().split(' ')))
b=0
if(a[1]==10):
    if(a[0]==1):
        print("-1")
    else:
        for i in range(0, a[0]-1):
            b+=(a[1]*(10**i))   
            b*=10
        print(b)
else:
    for i in range(0, a[0]):
        b+=(a[1]*(10**i))
    print(b)