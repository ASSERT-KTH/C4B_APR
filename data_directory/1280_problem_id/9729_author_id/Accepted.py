#!/usr/bin/env python3
# -*- coding: utf-8 -*-
k=int(input())
d=[int(a)for a in input().split()]
i=0
if k==0:
    print(0)
else:
    while True:
        a=max(d)
        k-=a
        d.remove(a)
        i+=1
        if k<=0:
            print(i)
            break
        if len(d)==0:
            print(-1)
            break