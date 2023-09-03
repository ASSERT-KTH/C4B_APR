from sys import stdin
n=int(stdin.readline().rstrip("\n"))
if n==1:
	print("1")
else:
	for i in range(2,n+1):
		print(i,end=" ")
	print("1")