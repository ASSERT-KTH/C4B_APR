#!/usr/bin/env python3

s = input()

counter = 0

for c in s:
	if c == '1':
		counter += 1

print(oct(counter)[2:])