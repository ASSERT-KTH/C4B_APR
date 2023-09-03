#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 08:09:05 2017

@author: lawrenceylong
"""

a,b,c = map(int,input().split())

print(min([2*(a+b),a+b+c,2*(b+c),2*(a+c)]))