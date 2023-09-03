'''
Created on 2017. 7. 10.

@author: KTH
ID: 133A. HQ9+
'''

pList = ["H","Q","9"]

inword = input()

f = False

for p in pList:
    if p in inword:
        f = True
        break
if(f):
    print("YES")
else:
    print("NO")