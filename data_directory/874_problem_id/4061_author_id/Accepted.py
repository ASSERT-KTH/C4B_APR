n,k=map(int,input().split())
v=1
p=1
for i in range(n-1) :
    p=p*2
while p!=k :
    if k>p :
        k=k-p
    p=p//2
    n=n-1
print(n)