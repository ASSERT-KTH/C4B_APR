import math
n,k=[int(f)for f in input().split()]
if math.floor(n/k)%2==1:
    print('YES')
else:
    print('NO')