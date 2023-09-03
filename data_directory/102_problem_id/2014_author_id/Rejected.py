d1,d2,d3=map(int,input().split())

a=d1+d1+d2+d2
c=d1+d3+d2
if a>c:
    print(c)
else:
    print(a)