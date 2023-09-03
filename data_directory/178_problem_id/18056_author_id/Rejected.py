from math import *
from sys import *
from decimal import *

l,r,k=(int(z) for z in stdin.readline().split())
k1=1
while k1<=r:
    if k1>=l:
        stdout.write(str(k1)+" ")
    k1 *= k
stdout.write("\n")