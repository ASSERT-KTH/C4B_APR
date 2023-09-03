x=input()
test='0'
i=0
y=0
while i<len(x):
    if test==x[i]:
        y+=1
        if y==7:
            print ("YES")
            break
    else:
        y=1
        test==x[i]
    i+=1
else:
    print("NO")