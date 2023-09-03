#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:45:02 2017

@author: lawrenceylong
"""

a,b,c = map(list(input()).count,["H","Q","9"])
print("YES") if a== 1 or b==1 or c ==1 else print("NO")