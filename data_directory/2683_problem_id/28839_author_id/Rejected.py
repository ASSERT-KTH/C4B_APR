a,b,c,d=int(input()),int(input()),int(input()),int(input())
e= (a or b) and (c^d)
f=(b and c)^(a or d)
print(e or f)