x = input()
x = x.split()
y = []
z = ""
for i in range(int(x[0]),int(x[2])):
    if i%int(x[1]) == 0:
        if i-(int(x[0])) not in y:
            y.append(i-int(x[0]))
if len(y) == 0:
    print(-1)
else:
    for i in range(0,len(y)):
        z+=str(y[i])+" "
    print(z)