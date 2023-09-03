# -*- coding: utf-8 -*-
a,b = map(int, input().split(' '))
if abs(a-b)==1 or a==b:
    print("YES")
else:
    print("NO")