n = int(input())
k = 0
for i in range(1,n+1):
	if i%2:
		k+=1
		if k==n:
			print(i)
			exit()
	k+=1
	if k==n:
			print(i)
			exit()