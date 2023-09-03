from math import ceil
n=int(input())
a=['','Sheldon','Leonard','Penny','Rajesh','Howard']
k=1
s=1
while 5*s<n:
    k*=2
    s+=k
s-=k
n=n-5*s
n=ceil(n/k)
print(a[n])