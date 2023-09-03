n,m=[int(i) for i in input().split()]
d=0
for i in range(n+1):
    d=d+i
c=d-m
if c<0:
    print(0)
else:
    print(c)