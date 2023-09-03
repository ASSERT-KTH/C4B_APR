def compute():
	a,b = map(int,input().split())
	if a == 0 and b == 0 : 
		return 'NO'
	if abs(a-b) <= 1 : 
		return 'YES'
	else: return 'NO'
print(compute())