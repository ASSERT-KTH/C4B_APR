n,a,b,c=[int(input())for _ in '1234']
r=0
if b-c<a:
	r=n//(b-c)-b//(b-c);n-=r*(b-c)
	while b<=n:t=n//b;r+=t;n=n%b+t*c
print(r+n//a)