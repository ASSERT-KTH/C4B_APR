x = int(input())
a = "Sheldon"
b = "Leonard"
c = "Penny"
d = "Rajesh"
e = "Howard"
z = 5
zz = 0
lst = [0]

while(zz<x):
    zz += z
    z *= 2
    lst.append(zz)
    
k = lst[len(lst)-2]
kk = k
l = k + 5
y = 0

for n in range(len(lst)-1):
    if(y==0):
        y += 1
    else:
        y *= 2

while(k<l):
    kk += y
    if(x <= kk):
        break
    k += 1

m = (k+1) % 5
if(m == 1):
    print(a)
elif(m == 2):
    print(b)
elif(m == 3):
    print(c)
elif(m == 4):
    print(d)
elif(m == 0):
    print(e)