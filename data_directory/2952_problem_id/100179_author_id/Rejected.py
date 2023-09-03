n,k=input().split()
t=0
n=int(n)
k=int(k)
while n>=k:
	n=n-k
	t=t+1
if t%2 == 0 :
	print('NO')
else:
	print('YES')