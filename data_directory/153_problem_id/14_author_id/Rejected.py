def pasha(m,n,x):
    m = m + 2    
    if m >= n:
        print(x)
    else:
        x = x + 1
        pasha(m,n,x)

z = int(input())

m = 0
if z%2 != 0:
    print(0)
else:
    x = 0
    n = z/2
    pasha(m,n,x)