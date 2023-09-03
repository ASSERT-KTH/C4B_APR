import math
n,k=map(int,input().split())
s=int (n/k)
if s%2 != 0:
    print('YES')
else:
    print('NO')