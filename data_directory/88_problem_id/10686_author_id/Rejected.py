n = int(input())
a = []
for _ in range(n):
    x,y = map(int,input().split())
    a.append((x,y))

#print(a)
for i in range(1,n):
    if a[0][0]!=a[i][0] and a[0][1] != a[i][1]:
        print(abs(a[i][0]-a[0][0]) * abs(a[i][1] - a[0][1]))
        exit()
print(-1)