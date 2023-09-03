# -*- coding: utf-8 -*-
a,b = map(int, input().split(' '))
if a==b==0:
    print("NO")
elif abs(a-b)==1 or a==b:
    print("YES")
else:
    print("NO")