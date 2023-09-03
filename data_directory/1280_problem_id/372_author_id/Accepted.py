k=int(input())
a=sorted(list(map(int,input().split())),key=int)
s,i=0,0
while s<k and i>-12:
        i-=1
        s+=a[i]
if s>=k:print(-i)
else:print("-1")