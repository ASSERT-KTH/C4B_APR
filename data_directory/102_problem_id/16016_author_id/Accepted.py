d1,d2,d3 = map(int,input().split())
s=[]
if(d1<d2):
    s.append(d1+d3+d2)
    s.append(d1*2+d2*2)
    s.append(d1*2+d3*2)
else:
    s.append(d1+d3+d2)
    s.append(d1*2+d2*2)
    s.append(d2*2+d3*2)
print(min(s))