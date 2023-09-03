import sys
n, m = map(int, input().split())
l=m-1
r=n+1
ans=0
if n==1:
	ans=1
else: 
	if m<n:
		while l<=r:
			mid=(l+r)/2
			i=int(mid)
			x=(i-m-1)*m+n
			y=((i-m)*(i+m+1))/2 
			if y>=x :
				ans=i
				r=i-1
			else :
				l=i+1
			
	else:
		ans=n 
print(int(ans))