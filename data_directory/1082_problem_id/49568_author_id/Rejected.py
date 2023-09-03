from math import log
k = int(input())
l = int(input())

ans = log(l, k)
if ans==int(ans):
    print ("YES")
    print (int(ans)-1)
else:
    print ("NO")