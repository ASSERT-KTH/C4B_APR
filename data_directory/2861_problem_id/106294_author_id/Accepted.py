def f(n,m):
    res = []
##    a = ceil(log(10**18,x))
##    b = ceil(log(10**18,y))
    for i in range(60):
        for h in range(60):
            res.append(x**i+y**h)
    res.append(n-1)
    res.append(m+1)
    return list(set(res))

x,y,l,r = map(int, input().split(' '))
unh = f(l,r)
unh.sort()
res = 0
for i in range(len(unh)-1):
    if l-1 <= unh[i] <= r+1 and l-1 <= unh[i+1] <= r+1:
        res = max(res, unh[i+1]-unh[i])
print(res-1)