from math import ceil
m,n,a=map(int,input().split())
times=ceil(m/a)*ceil(n/a)
print(times)