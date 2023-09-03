#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:12:40 2017

@author: lawrenceylong
"""

from math import *

a,b,c = map(int,input().split())
turn = 0
while c > 0:
    if turn %2 == 0:
        c -= gcd(a,c)
    else:
        c-= gcd(b,c)
    turn +=1
print((turn+1)%2)