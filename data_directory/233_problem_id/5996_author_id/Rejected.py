def f(n, a, b, c):
	if a<=b-c:
		return n//a
	ans=0
	while n>=b:
		t=n//b
		n-=(b-c)*t
		ans+=t
	return ans+n//a
import sys
print(f(*map(int, sys.stdin.read().split())))