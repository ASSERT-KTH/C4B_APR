a,x,y=map(int,input().split())
if y>0 and y%a!=0 and x>-a and x<a:
    if y//a==0 or y//a==1 or y//a==2 :
        if y//a==0:
            if x>-a/2 and x<a/2:
                print(1)
                exit()
            else:
                print(-1)
                exit()
        elif y//a==1:
            if x>-a/2 and x<a/2:
                print(2)
                exit()
            else:
                print(-1)
                exit()
        else:
            if x==0:
                print(-1)
                exit()
            if x>0:
                print(4)
                exit()
            else:
                print(3)
                exit()
    else:
        z=(y-3*a)//(2*a)
        ans=4+3*z
        k=y-3*a-2*a*z
        if k<a:
            if x>-a/2 and x<a/2:
                ans+=1
            else:
                print(-1)
                exit()
        elif k>a:
            ans+=2
            if x>0:
                ans+=1
            if x==0:
                print(-1)
                exit()
        print(ans)
        exit()
print(-1)