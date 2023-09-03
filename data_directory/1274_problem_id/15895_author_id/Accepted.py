#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 08:20:36 2017

@author: lawrenceylong
"""
z=input;i=int;n=[i(z()) for r in ' '*4]
print(sum([any([x%y<1 for y in n]) for x in range(1,i(z())+1)]))