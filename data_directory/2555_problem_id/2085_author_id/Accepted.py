a=input()
b=0
c=False
d=0
for r in a:
    if(r=="0"):
        b+=1
        if(b==7):
            c=True
            break
    else:
        b=0
    if(r=="1"):
        d+=1
        if(d==7):
            c=True
            break
    else:
        d=0
    

    

if(c):
    print("YES")
else:
    print("NO")