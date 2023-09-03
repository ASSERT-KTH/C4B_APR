x=input()
i=0
p=0
l=""
for h in "hello":
    while h!=l and i<len(x):
        l=x[i]
        i+=1
    if i!=len(x) or h=="o" and l=="o":
        p+=1
if p==5:
    print("YES")
else:
    print("NO")