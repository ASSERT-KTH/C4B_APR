a,b=map(int,input().split())
c,d=map(int,input().split())
z=-1
for i in range(2000):
    for j in range(2000):
        if a*i+b == c*j+d:
            z=a*i+b
            break
    if z!=-1:
        break
print(z)