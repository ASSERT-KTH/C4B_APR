from math import log, ceil

k,b,n,t = map(int, input().split())

if k == 1:
    print(max(0, ceil((1+b*n-t)/b)))
else:
    print(max(0, ceil(n-log((t-t*k-b)/(1-k-b),k))))