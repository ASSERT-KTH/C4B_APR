#!/usr/bin/python3
n = int(input());
week = [int(x) for x in input().split()];
s = sum(week);
n %= s;
if (n):
	i=0;
	while(n > week[i]):
		n -= week[i];
		i += 1;
		print(i+1);
else:
	print(7);