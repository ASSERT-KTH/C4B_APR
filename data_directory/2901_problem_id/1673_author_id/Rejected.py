c,v0,v1,a,l = map(int,input().split())
t = v0
k = 1
while t < c:
    if v0 >= v1:
        v0 = v1
    else:
        v0 = v0 + a
    t = t - l + v0
    k += 1
print(k)