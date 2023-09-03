from math import *
n,m,a=map(float,input().strip().split())
print(ceil(n/a)+(ceil((m-a)/a)*ceil(n/a)))