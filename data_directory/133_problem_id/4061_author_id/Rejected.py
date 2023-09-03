l=list(map(int,input().split()))
l1=list(map(int,input().split()))
k=0
k1=0
if l[0]-l1[0]<0 :
    k=k+abs(l[0]-l1[0])
else :
    k1=k1+abs(l[0]-l1[0])
if l[1]-l1[1]<0 :
    k=k+abs(l[1]-l1[1])
else :
    k1=k1+abs(l[1]-l1[1])
if l[2]-l1[2]<0 :
    k=k+abs(l[2]-l1[2])
else :
    k1=k1+abs(l[2]-l1[2])
if abs(k1-1)//2>=k :
    print('Yes')
else :
    print('No')