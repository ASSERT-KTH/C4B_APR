#!/usr/bin/python

import sys
y,k,n=map(int,sys.stdin.readline().split())
index=int(y/k)*k +k
x=0
while (index <= n):
	x=index-y
	index+=k
	if(x==0):
		continue
	print(str(x)+" ",end="")
	


if(x==0):
	print("-1")