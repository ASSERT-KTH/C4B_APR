from math import inf
a, b = [int(x) for x in input().split()]
c, d = [int(x) for x in input().split()]
if b > d:
    a, c = c, a
    b, d = d, b
r1 = (d-b) % a
r2 = c % a
k2s = [(r1+k2*r2) % a for k2 in range(a)]
if 0 not in k2s:
    print(-1)
else:
    
    print(k2s.index(0)*c+d)