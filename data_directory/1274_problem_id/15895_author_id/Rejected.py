#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 08:20:36 2017

@author: lawrenceylong
"""

skip = []
for i in range(4):
    a = int(input())
    if a not in skip:
        skip.append(a)
d = int(input())
counted = []
for i in range(4):
    for a in range(1,d+1,skip[i]):
        if a not in counted:
            counted.append(a)
print(len(counted))