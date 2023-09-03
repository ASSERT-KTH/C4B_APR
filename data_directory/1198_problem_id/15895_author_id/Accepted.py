#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:45:02 2017

@author: lawrenceylong
"""

a,b,c = map(list(input()).count,["H","Q","9"])
print("YES") if a> 0 or b>0 or c >0 else print("NO")