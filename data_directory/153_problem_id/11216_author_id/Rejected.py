from math  import ceil
n = int(input())
if n&1 == 0:
	ans = 0
else :ans = ceil(n/4)-1
print(ans)