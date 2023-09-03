a=[int(i) for i in input().split()]
t=0
while a[0]>0 and a[1]>0:
    if a[1]>a[0]:
        a[0]+=1
        a[1]-=2
    else:
        a[0]-=2
        a[1]+=1
    t+=1
print(t)