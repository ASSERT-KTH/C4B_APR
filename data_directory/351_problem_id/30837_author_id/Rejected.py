import math
from math import floor

a11 = input()
a21 = input()
b11 = input()
b21 = input()


sList = []
sList.append(a11[0])
sList.append(a11[1])
sList.append(a21[0])
sList.append(a21[1])

sList.remove('X')
sList.append(sList[0])
sList.append(sList[1])

pList = []
pList.append(b11[0])
pList.append(b11[1])
pList.append(b21[0])
pList.append(b21[1])

pList.remove("X")

pList = pList[::-1]

s1 = s2 = ""

for i in sList:
    s1+=i
for i in pList:
    s2+=i
    
if(s1.find(s2) == -1):
    print("NO")
    
else:
    print("YES")