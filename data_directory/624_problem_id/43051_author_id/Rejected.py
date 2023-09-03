t,s,x = list(map(int, input().split()))

if t == x:
    print("YES")
    exit()

if (x-t)%s == 0 or ((x-t-1)%s == 0 and x >= s + t):
    print("YES")
else:
    print("NO")