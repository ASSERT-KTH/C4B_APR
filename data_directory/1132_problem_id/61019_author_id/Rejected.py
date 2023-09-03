x=int(input())
a=0
j=0
if (x%4==0) or (x%7==0):
    print("YES")
    j=1
x=str(x)
x=list(x)
if j==0:
    for k in range (len (x)):
        if "7" in x:
            y=x.index("7")
            x[y]="3"
            a+=1
        elif "4" in x:
            y=x.index("4")
            x[y]="3"
            a+=1
            
    if a==len(x):
        print("YES")
    else:
        print("NO")