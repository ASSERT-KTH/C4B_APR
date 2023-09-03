(n,m) = map(int, input().split())
if (n <= m):
    print (n)
else:
    aM = m
    n = n - m
    l = 0
    r = 2e9
    while (l < r):
        m = (l + r)/2
        val = m*(m+1) / 2
        if (val >= n):
            r = m
        else:
            l = m + 1
    print (l + aM)