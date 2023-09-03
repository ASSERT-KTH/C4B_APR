a=str(input())
n=list(a)
n.append(" ")

k=0
z=False
for k in range(len (n)):
    if n[k]=="1":
        t=0
        while n[k]=="1":
            k+=1
            t+=1
        if t>=7:
            z=True
        k+=1
    else:
        t=0
        while n[k]=="0":
            k+=1
            t+=1
        if t>=7:
            z=True
if z==True:
    print("YES")
else:
    print("NO")