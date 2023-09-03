n=int(input())
x=list(map(int,input().split()))
x=sorted(x,reverse=True)
count=0
sum=0
if sum<n:
    for i in range(len(x)):
        sum+=x[i]
        if sum>=n:
            print(i+1)
            import sys;sys.exit()
    print(-1)
    sys.exit()
print(0)