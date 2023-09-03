L = [int(s) for s in input().split()]
k,a,b = L[0],L[1],L[2]
if (b-a) % k == 0:
    if a % k == 0:
        print((b-a+k)//k)
    else:
        print((b-a)//k)
else:
    print((b-a)//k)