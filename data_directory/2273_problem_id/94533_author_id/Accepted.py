import math

nbr=int(input())
s=int(math.sqrt(2*nbr))
if nbr==s*(s+1)/2 or nbr==(s+1)*(s+2)/2:
    print("YES")
else:
    print("NO")