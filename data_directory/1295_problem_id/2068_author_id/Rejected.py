n, k, l, c, d, p, nl, np = map(int,input().split())
x=round((k*l-(k*l)%nl)/nl)
y=c*d
z=round(p/np)
if(x>y):
    if(y>z):
        print((int)(z/n))
    else:
        print((int)(y/n))
else:
    if(x>z):
        print((int)(z/n))
    else:
        print((int)(x/n))