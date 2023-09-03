n=int(input())
r=0
i=1
while i*i<n and i*4<n:r+=(n-i-i)%2==0;i+=1
print(r)