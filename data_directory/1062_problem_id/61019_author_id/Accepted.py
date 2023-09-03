s=int(input())
x=str(s)
count=0
for k in range (len(x)):
    if x[k]=="4" or x[k]=="7":
        count+=1
if count ==4 or count==7:
    print("YES")
else:
    print("NO")