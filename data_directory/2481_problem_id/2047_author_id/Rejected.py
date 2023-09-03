x = int(input())
a = "Sheldon"
b = "Leonard"
c = "Penny"
d = "Rajesh"
e = "Howard"

y = x/5
if(y%1 != 0):
    y = x//5 + 1
    
z = 0

i = 0
j = 1

lst = [0]

while(i<x):
    z += 5 * j
    i = z
    j += 1
    lst.append(z)

k = lst[len(lst)-2]
zz = lst[len(lst)-2]
l = k + 5

while(k<l):
    zz += (len(lst)-1)
    if(x <= zz):
        break
    k += 1
    
m = (k + 1) % 5
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