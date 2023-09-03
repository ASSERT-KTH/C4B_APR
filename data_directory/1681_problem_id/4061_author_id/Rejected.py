n,m=map(int,input().split())
k=0
for i in range(max(n,m)) :
    for j in range(max(n,m)) :
        if i*i+j==n and i+j*j==m :
            k=k+1
print(k)