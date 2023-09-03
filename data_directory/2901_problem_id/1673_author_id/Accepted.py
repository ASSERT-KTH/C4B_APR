c,v0,v1,a,l = map(int,input().split())
t = v0
k = 1
while t < c:
    v0 = v0 + a
    if v0 > v1:
        v0 = v1
    t = t - l + v0
    k += 1
print(k)