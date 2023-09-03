def solve(x,l1,r1,l2,r2):
	if x==0:return 1
	if l1>x:
		l1-=x+1
		r1-=x+1
	if l2>x:
		l2-=x+1
		r2-=x+1
	ans=max(0,min(r1,r2)-max(l1,l2)+1)
	if l1<=x and x<=r1 and l2<=x and x<=r2:
		if l1==0 or r1==x*2:
			ans=max(ans,max(x-12,r2-x))
		elif l2==0 or r2==x*2:
			ans=max(ans,max(x-11,r1-x))
		else:
			if l1<=x-1 and r2>=x+1:
				ans=max(ans,solve(x//2,l1,x-1,0,r2-x-1))
			if l2<=x-1 and r1>=x+1:
				ans=max(ans,solve(x//2,l2,x-1,0,r1-x-1))
	elif l1<=x and x<=r1:
		if l1==0 or r1==x*2:
			ans=max(ans,r2-l2+1)
		else:
			if l1<=x-1:
				ans=max(ans,solve(x//2,l1,x-1,l2,r2))
			if r1>=x+1:
				ans=max(ans,solve(x//2,0,r1-x-1,l2,r2))
	elif l2<=x and x<=r2:
		if l2==0 or r2==x*2:
			ans=max(ans,r1-l1+1)
		else:
			if l2<=x-1:
				ans=max(ans,solve(x//2,l2,x-1,l1,r1))
			if r2>=x+1:
				ans=max(ans,solve(x//2,0,r2-x-1,l1,r1))
	else:
		ans=max(ans,solve(x//2,l1,r1,l2,r2))
	return ans

l1,r1,l2,r2=map(int,input().split())
print(solve((1<<36)-1,l1-1,r1-1,l2-1,r2-1))