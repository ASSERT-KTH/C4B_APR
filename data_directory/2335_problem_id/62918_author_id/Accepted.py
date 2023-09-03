'''
Created on 2017. 7. 10.

@author: KTH
ID: 58A. Chat room
'''

t = "hello"

inword = input()

cnt = 0
f = False

for w in inword:
    target = t[cnt]
    if target == w:
        cnt += 1
    if cnt == len(t):
        f = True
        break

if(f):
    print("YES")
else:
    print("NO")