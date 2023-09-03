#!/usr/bin/env python3
d1,d2,d3 = [int(i) for i in input().split()]
res = min(d1+d2,d3,d1*2+d2*2)
res = min(res,d1*2+d3*2)
res = min(res,d2*2,d3*2)
print(res)