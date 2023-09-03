a,b=map(int,input().split())
r,l=map(int,input().split())
for i in range(0,101) :
    for j in range(101) :
        if a*i+b==l+r*j :
            print(a*i+b)
            exit()
print(-1)