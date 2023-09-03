a=input()
l=0
u=0
for i in a:
    if(i.islower()):
        l+=1
    else:
        u+=1

if(l>u):
    print(a.upper())
    
else:
    print(a.lower())