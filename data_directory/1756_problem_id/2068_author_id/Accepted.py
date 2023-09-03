a=[int(i) for i in input().split()]
i=0
while i<3:
    if(a[i]>a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]
        i=-1
    i+=1
k=0
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        k+=1
print(k)