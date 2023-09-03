a=input()
b=["h","e","l","l","o"]
c=0
d=0
for i in a:
    if(b[c]==i):
        c=c+1
        if(c==5):
            break
       
if(c==5):
    print("YES")
else:
    print("NO")