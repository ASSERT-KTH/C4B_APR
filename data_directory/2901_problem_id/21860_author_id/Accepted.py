a,b,c,d,e=map(int,input().split())
a=a-b
k=1
r=1
while a>0 :
    k=k+1
    a=a-min(b+(d*r),c)+e
    r=r+1
print(k)