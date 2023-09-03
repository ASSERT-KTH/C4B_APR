a,b,c,d=int(input()),int(input()),int(input()),int(input())
e= (a ^ b) and (c or d)
f=(b and c)or(a ^ d)
print(e^f)