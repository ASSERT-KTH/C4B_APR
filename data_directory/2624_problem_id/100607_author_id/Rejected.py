n = int(input())
ans = ''
if n % 2 == 0:
	for i in range(n//2):
		ans += '1'
else:
	for i in range(n//2-1):
		ans += '1'
	ans += '7'
print(ans)