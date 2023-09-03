x=int(input())
if x<3:
    print(-1)
else:
    if x%2==0:
        x=int(x/2)
        q=1
        b=x
        c=1
        for j in range(3,x,2):
            if j%2 and int(x/j)%2:
                q=0
            if x%j==0 and q:
                b=int(j)
                c=int(x/j)
                break
            q=1
        print(b*b -c*c,b*b+c*c)
    else:
        b=x
        c=1
        for j in range(3,x,2):
            if x%j==0 and int(x/j)%2:
                b=int(j)
                c=int(x/j)
                break
        print(int((b*b-c*c)/2),int((b*b+c*c)/2))