t,s,k = map(int, input().split())

t-=1
k-=1

sat=[0]*1000000
for i in range(t,k+s,s):
    sat[i]=1
    if i!=t:
        sat[i+1]=1

print("YES" if sat[k]==1 else "NO")