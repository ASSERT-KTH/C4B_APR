#!/usr/bin/python

import sys

n = int(input())
if n % 2 == 0:
    result = int(n/2-1)
else:
    result = int(n/2-1) + 1
print(result)