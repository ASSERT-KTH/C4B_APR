var=input("")
var=var.split(" ")
n,a,b,p,q=int(var[0]),int(var[1]),int(var[2]),int(var[3]),int(var[4])
if p>q:
    x,y=a,b
    mx,mn=p,q
else:
    x,y=b,a
    mx,mn=q,p
s=0
j=int(n/x)
s+=mx*j
k=int(n/y)
for i in range(1,k+1):
    if ((i*y)%x)!=0:
        s+=mn    
print(s)