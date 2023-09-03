from math import log
n = int(input())
m=int(input())
imp = log(m)/log(n)
if imp==int(imp):
    print("YES")
    print(int(imp)-1)
else:
    print("NO")