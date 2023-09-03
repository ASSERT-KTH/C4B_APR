#!/usr/bin/python

import sys
y,k,n=map(int,sys.stdin.readline().split())
index=k
while (index < y ):
	index+=k
x=0
while (index <= n):
	x=index-y
	index+=k
	if(x==0):
		continue
	print(str(x)+" ",end="")
	


if(x==0):
	print("-1")