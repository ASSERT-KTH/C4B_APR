k=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
c=0
f=0
for i in range(12):
    if c<k:
        c+=a[i]
        f+=1
    if c>=k:
        break
if c>=k:
    print(f)
else:
    print(-1)