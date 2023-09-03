a,b,c = (int(i) for i in input().split())
s = 0
while (True):
    for i in range(c,0,-1):
        if (a%i==0 and c%i==0):
            s = i
            continue
    c -=s
    if (c<0):
        print(1)
        exit(0)
    elif(c==0):
        print(0)
        exit(0)
    for i in range(c,0,-1):
        if (b%i==0 and c%i==0):
            s = i
            continue
    c -=s
    if (c<0):
        print(0)
        exit(0)
    elif(c==0):
        print(1)
        exit(0)