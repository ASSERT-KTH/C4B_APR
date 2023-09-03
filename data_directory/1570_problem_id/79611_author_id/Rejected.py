from math import log, ceil

k,b,n,t = map(int, input().split())

if k == 1:
    print(max(0, ceil((t+bn-1)/b)))
else:
    print(max(0, ceil(n-log((t-t*k-b)/(1-k-b),k))))