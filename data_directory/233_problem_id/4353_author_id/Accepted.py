n,a,b,c=[int(input())for _ in '1234']
r=0
if b-c<a:
	r=n//(b-c)-b//(b-c)
	if r<0:r=0
	n-=r*(b-c)
	while b<=n:t=n//b;r+=t;n=n%b+t*c
print(r+n//a)