s = input()
l = list(s)
#print(l)
temp = []
flag = 0
h = -1
e = 0
L = 0
countl = 0
o = 0
for i in range(len(l)):
    if l[i]=="h" and h == -1:
            temp.append(l[i])
            h = i
            break
#print(h)
if h != -1:
    for i in range(h, len(l)):
        if l[i]=="e" and e == 0:
            temp.append(l[i])
            e = i
            break
else:
    flag = 1
#print(e)
if e!=0:
    for i in range(e, len(l)):
        if l[i]=="l" and countl!=2:
            temp.append(l[i])
            countl+=1
            L = i
else:
    flag = 1
#print(countl)
#print(L)
if countl==2:
    for i in range(L, len(l)):
        if l[i]=="o":
            temp.append(l[i])
            o = i
            break
else:
    flag = 1

if o == 0:
    flag = 1
#print(temp)
if flag == 0:
    print("YES")
else:
    print("NO")