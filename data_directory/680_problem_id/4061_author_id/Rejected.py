n=int(input())
if n==1 or n==2 :
    print(-1)
if n%2==0 :
    print((n*n//4-1),(n*n//4+1))
else :
    print(n*n//2,(n*n//2)+1)