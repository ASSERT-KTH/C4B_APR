n,k = [int(i) for i in input().split()]
if k >= n//2:
    print (n*(n-1)//2)
else:
    ans = (n-1+n-k) * (k) // 2
    ans = ans * 2 - k*k
    print (ans)