n,m = map(int,input().split())
z=0
for x in range(1,n+1):
    for y in range(1,m+1):
        if (x+y)%5==0:
            z+=1
print(z)