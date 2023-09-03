x=[int(y) for y in input()]
i=0
while i<len(x):
    if x[i]!=7 and x[i]!=4:
        print ("NO")
        break
    i+=1
else:
    print("YES")