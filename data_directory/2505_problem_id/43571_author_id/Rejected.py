a,b = input().split(" ")
a = int(a)
b = int(b)
z = a<b
if(z):
    d = 1
    m = 0
else:
    d = 0
    m = 1
t = 0
while(d < b or m < a):
    t += d*a - m*b
    if(z):
        z = not z
        while(d*a >= m*b):
            m += 1
    else:
        z = not z
        while(d*a <= m*b):
            d += 1
if(t>0):
    print("Masha")
elif(t<0):
    print("Dasha")
else:
    print("Equal")