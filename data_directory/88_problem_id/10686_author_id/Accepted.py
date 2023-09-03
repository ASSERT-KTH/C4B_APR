n = int(input())
a = []
for _ in range(n):
    x,y = map(int,input().split())
    a.append((x,y))

#print(a)
for i in range(n):
    for j in range(n):
        if a[i][0]!=a[j][0] and a[i][1] != a[j][1]:
            print(abs(a[i][0]-a[j][0]) * abs(a[i][1] - a[j][1]))
            exit()
print(-1)