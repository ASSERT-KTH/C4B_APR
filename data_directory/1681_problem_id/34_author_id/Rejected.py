n,m=map(int, input().split())
res=0
for i in range(int(n**0.5)+1):
    for j in range(n):
        if i**2+j==n and i+j**2==m:
            res+=1
print(res)