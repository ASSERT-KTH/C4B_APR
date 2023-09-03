f=[1,1]
n=int(input())
i=0
while f[0]+f[1]<=n:
    i+=1
    f[0],f[1]=f[1],f[0]+f[1]

print(i)