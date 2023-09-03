f=[1,1]
n=int(input())
i=0
while f[0]+f[1]<n:
    i+=1
    f[0],f[1]=f[1],f[0]+f[1]
if n==2: i=1
if n==3: i=2
print(i)