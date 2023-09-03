#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 08:23:58 2017

@author: lawrenceylong
"""

a = int(input())
b = list(map(int,input().split()))
b.sort(reverse=True)
count = 0
k = 0
yes = True
while count < a:
    count += b[k]
    k+=1
    if k == 12:
        if sum(b) < a:
            print(-1)
            yes = False
        break
if yes:
    print(k)