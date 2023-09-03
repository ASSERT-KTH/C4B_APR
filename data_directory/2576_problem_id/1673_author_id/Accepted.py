k,a,b = map(int,input().split())
l = a // k
p = b // k
if l == 0:
    if b % k == 0:
        if l + p != 0:
            print(l + p)
        else:
            print('-1')
    else:
        print('-1')
elif p == 0:
    if a % k == 0:
        if l + p != 0:
            print(l+p)
        else:
            print('-1')
    else:
        print('-1')
else:
    print(l+p)