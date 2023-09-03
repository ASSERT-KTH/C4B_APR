n,k = [int(i) for i in input().split()]
if k >= n//2:
    print (n*(n-1)//2)
else:
    ans = 0
    for i in range(k):
        ans += n-i-1
    ans *= 2
    ans -= k
    print (ans)