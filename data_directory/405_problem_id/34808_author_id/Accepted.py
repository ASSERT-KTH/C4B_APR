#!/usr/bin/env python3

s = oct(int(input()))

counter = 0

for c in s:
	if c == '1':
		counter += 1

print(counter)