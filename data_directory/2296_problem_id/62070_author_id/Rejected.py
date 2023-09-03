domino=0
m,n=map(int,input().split())
if n%2==0:
    domino=n/2*m
elif m%2==0:
    domino=m/2*n
else:
    for i in range(n):
        domino=m//2*n+n//2
int(domino)
print(domino)