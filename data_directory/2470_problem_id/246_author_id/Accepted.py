n,m=list(map(int,input().split()))

c=n+1

while c<=m:


    for i in range(c-1,1,-1):
        if c%i==0:

            break
    else:

        if c<m:
            print('NO')
        elif c==m:
            print('YES')
        exit()


    c+=1
else:
    print('NO')