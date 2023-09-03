#1 3 2
#1 1 2 2
#1

#2 3 1
#2 2 1 1
#

d1,d2,d3 = map(int,input().split())
s=0
if(d1<d2):
    s=d1
    if(s+d3+d2<s+d1+d2*2):
        s+=d3+d2
    else:
        s+=d1+d2*2
else:
    s = d2
    if (s+d3 + d1 <s+ d2 + d1 * 2):
        s += d3 + d1
    else:
        s += d2 + d1 * 2
print(s)