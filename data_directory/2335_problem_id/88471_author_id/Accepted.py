# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 02:15:46 2017

@author: www
"""
f = False
s = input()
w = "hello"
k = 0
for i in s:
    if k == 5:
        f = True
        break
    if i == w[k]:
        k += 1
if k == 5 or f:
    print("YES")
else:
    print("NO")