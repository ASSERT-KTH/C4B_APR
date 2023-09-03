R=range
m=['' for i in R(8)]
for _ in R(8):
    v=input()
    for j in R(8):m[j]+=v[j]
a=b=9
for s in m:
    x=[s[::-1].find('B'),s[::-1].find('W'),s.find('W'),s.find('B')]
    for i in 0,1,2,3:x[i]=[x[i],9][x[i]<0]
    if x[0]<x[1]:b=min(b,x[0])
    if x[2]<x[3]:a=min(a,x[2])
print('AB'[b<a])