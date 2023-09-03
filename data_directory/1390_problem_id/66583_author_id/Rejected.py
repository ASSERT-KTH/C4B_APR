import math

a=input()
p=a.split()
n=float(p[0])
x=float(p[1])
y=float(p[2])

out=math.ceil((y/100)*n)


print (int(out-x))