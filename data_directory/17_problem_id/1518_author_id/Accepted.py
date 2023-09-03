a=list(map(int, input().strip().split(' ')))

if(a[1]==10):
    if(a[0]==1):
        print("-1")
    else:
        for i in range(0, a[0]-1):
            print("1", end='', sep='')
        print("0")
else:
    for i in range(0,a[0]):
        print(a[1], end='', sep='')