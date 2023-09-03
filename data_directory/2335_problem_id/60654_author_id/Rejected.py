a = input()

a=list(a)
t=""
j=0
for x in a:
    if len(t)<1:
        t=t+x
    else:
        if t[len(t)-1:] != x:
            t=t+x

        if x == "l" and t[len(t)-1:]== "l" and j==0:
            t=t+x
            j=1
        if x!= "l":
            j=0
            
            
    
if   t.find("hello")  >0:
    print("YES")
else:
    print("NO")