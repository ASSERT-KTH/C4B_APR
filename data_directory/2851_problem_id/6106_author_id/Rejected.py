s=input()
l=s.split()
v1=int(l[0])
v2=int(l[1])
i=1
while v1>0 and v2>0 :
    if i%2==1:
        v1-=i
    if i%2==0:
        v2-=i
    i+=1
if v1<0 :
    print("Vladik")
else :
    print("Valera")