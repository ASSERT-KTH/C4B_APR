from sys import stdin
n=int(stdin.readline().rstrip("\n"))
if n==1:
	print("1")
else:
	print(n,end=" ")
	for i in range(1,n):
		print(i,end=" ")
	print("")