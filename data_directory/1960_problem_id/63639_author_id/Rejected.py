a=[]
for i in range(5):
    a.append([int(i) for i in input().split()])
for i in range(5):
    for j in range(5):
        if a[i][j]==1:
            z=i
            d=j
print(abs(z-i)+abs(d-j))