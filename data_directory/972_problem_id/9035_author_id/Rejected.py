a = [int(i) for i in input().split()]

if a[0]-a[1]>=-1 and a[0]-a[1]<=1 and a[1]>0:
    print("YES")
else:
    print("NO")