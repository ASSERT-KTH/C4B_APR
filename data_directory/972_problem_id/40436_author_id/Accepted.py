a = [int(i) for i in input().split()]
p = int(a[0])
n = int(a[1])

if p==n+1 or p==n or n==p+1:
    if p==0 and n==0:
        print("NO")
    else:
        print("YES")
else:
    print("NO")