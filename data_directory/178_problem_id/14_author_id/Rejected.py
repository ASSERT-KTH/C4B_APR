#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import math

txt=input()
nums=txt.split(" ")
l=int(nums[0])
r=int(nums[1])
k=int(nums[2])
q=1
while q<=l:
	q=q*k
if q>=r:
	print("-1", end="")
	exit()
print("%d" % q, end="")
q=q*k
while q<r:
	print(" %d" % q, end="")
	q=q*k