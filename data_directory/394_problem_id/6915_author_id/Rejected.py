n,k=[int(i) for i in input().split()]
m=0 if k>=2*n else n-2*k
print((n*(n-1)-m*(m-1))//2)