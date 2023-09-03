t, s, x = [int(x) for x in input().split()]
if ((x-t)%s==0 or (x-t-1)%s==0) and x>=t+s or x==t:
    print("YES")
else:
    print("NO")