n = int(input())
a = list(map(int,input().split(" ")))
a.sort()
cnt=0
x=12
while(n>0 and x>0):
	n-=a[x-1]
	x-=1
	cnt+=1
if x>=0 and n<=0:
	print(cnt)
else:
	print(-1)