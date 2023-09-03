n,m = map(int,input().split())
z=0
for x in range(n):
    z+=(m+((x+1)%5))//5
print(z)