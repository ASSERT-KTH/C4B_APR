a=[int(x) for x in input().split(" ")]
if a[0]==max(a):
    print(a[1]*2+a[2]*2)
elif a[1]==max(a):
    print(a[0]*2+a[2]*2)
else:
    print(a[0]*2+a[1]*2)