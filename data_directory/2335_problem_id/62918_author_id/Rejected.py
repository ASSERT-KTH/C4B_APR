'''
Created on 2017. 7. 10.

@author: KTH
ID: 58A. Chat room
'''

t = "hello"

inword = input()

cnt = 0

for w in inword:
    if cnt == len(t):
        print("YES")
        break
    target = t[cnt]
    if target == w:
        cnt += 1
                
if cnt < len(t):
    print("NO")