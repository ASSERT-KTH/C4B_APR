t,s,x = list(map(int, input().split()))

if t == x:
    print("YES")
    exit()
if x < s + t:
    print("NO")
    exit()
if (x-t)%s == 0 or (x-t-1)%s == 0:
    print("YES")
else:
    print("NO")