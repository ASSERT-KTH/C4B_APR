k=int(input())
a=sorted(map(int,input().split()))
a.reverse()
s=r=0

if(k>0):
    for i in a:
        s+=i
        r+=1
        if(s>=k):
            print(r)
            break
    if(s<k):
        print(-1)
else:
    print(0)