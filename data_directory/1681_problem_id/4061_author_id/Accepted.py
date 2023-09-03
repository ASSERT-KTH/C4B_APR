n,m=map(int,input().split())
k=0
for i in range(0,max(n,m)+1) :
    for j in range(0,max(n,m)+1) :
        if i*i+j==n and i+j*j==m :
            k=k+1
print(k)