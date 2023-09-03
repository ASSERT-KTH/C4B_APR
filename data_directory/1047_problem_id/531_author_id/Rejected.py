'''input
07:07
'''
h, m = input().split(":")
if h[::-1] > m and h[::-1] < "60":
	print(h, h[::-1], sep=":")
elif h < "23":
	h = str(int(h) + 1)
	while h[::-1] >= "60":
		h = str(int(h) + 1)
	print(h, h[::-1], sep=":")
else:
	print("00:00")