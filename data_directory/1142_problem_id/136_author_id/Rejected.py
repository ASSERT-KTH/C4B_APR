n,a,b=[int(i) for i in input().split()]
t=0
for i in range(n):
    if i>=a and i<=b:
        t+=1
print(t+1)