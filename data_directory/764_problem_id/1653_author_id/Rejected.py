#!/bin/python3

x1, x2, x3 = [int(i) for i in (input().split())]
avg = (x1+x2+x3)//3
print(abs(avg-x1)+abs(avg-x2)+abs(avg-x3))