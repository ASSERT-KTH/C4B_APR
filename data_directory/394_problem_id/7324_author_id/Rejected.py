n1=input().split()
n=int(n1[0])
k=int(n1[1])
if k >= n//2:
    print(n*(n-1)//2)
else:
    print(k*k+2*k*(n-2*k)+k)