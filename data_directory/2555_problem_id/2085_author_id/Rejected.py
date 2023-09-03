a=input()
b=0
c=False
for r in a:
    if(r=="0"):
        b+=1
        if(b==7):
            c=True
            break
    else:
        b=0

if(c):
    print("YES")
else:
    print("NO")