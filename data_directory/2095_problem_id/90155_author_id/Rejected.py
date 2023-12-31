#cf288b.py
import sys
(n,k)=map(int,sys.stdin.readline().split())
mod_prime=1000000007
f=[0]*k 
#f(x)= the number of ways that a group of x elements eventually leads to 1 (1 is not part of the group and does not points to anywhere)
f[0]=1
f[1]=1
c=[[1 for j in range(i+1)] for i in range (k)]
for i in range(1,len(c)):
	for j in range(1,len(c[i])-1):
		c[i][j]=(c[i-1][j-1]+c[i-1][j])%mod_prime
#print (c)
for x in range(2,k):
	f[x]=0
	for i in range(0,x):
		f[x]+=c[x-1][i]*f[i]*f[x-1-i]*(i+1)%mod_prime
		#print("x={0},i={1},f[x]={2}".format(x,i,f[x]))

ans=(k*f[k-1]*(n-k)**(n-k))%mod_prime
#print(f)
print(ans)