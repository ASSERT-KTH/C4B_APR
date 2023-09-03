from sys import stdin
t,s,x = map(int,stdin.readline().split())
i = 1
res = 0
while(res < x):
    res = t
    if(res >= x):
        break
    res = t + s * i
    if (res >= x):
        break
    res = t + s * i + 1
    if (res >= x):
        break
    i += 1

if(res != x):
    print("NO")
else:
    print("YES")