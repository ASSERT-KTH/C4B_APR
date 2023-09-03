k=int(input())
x=sorted(list(map(int,input().split())))
c,s=0,0
for i in range(11,-1,-1):
    if s>=k:
        break
    s+=x[i]
    c+=1
print(c)