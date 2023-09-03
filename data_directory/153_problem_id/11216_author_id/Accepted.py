from math  import ceil
n = int(input())
if n&1 == 0:
	ans = ceil(n/4)-1
else :ans = 0
print(ans)