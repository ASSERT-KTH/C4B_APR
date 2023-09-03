#!/usr/bin/python3.5

a = [int(x) for x in input().split(" ")]
a.sort()

dist = a[2] - a[0]

print(dist)