d1,d2,d3=map(int,input().split())
if(d1<d2):
    if(2*d1+d2<d3):
        print(2*d1+2*d2)
    else:
        print(d1+d2+d3)
else:
    if(2*d2+d1<d3):
        print(2*d2+2*d1)
    else:
        print(d1+d2+d3)