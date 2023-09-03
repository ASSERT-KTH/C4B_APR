import math

n = int(input())

ans = 0

for x in range(1,n):
    ans += x*(n-x)

ans += n
print (ans)