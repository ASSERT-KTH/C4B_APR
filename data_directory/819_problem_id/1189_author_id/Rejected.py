last, res = -1, 0
s = input()
for i, c in enumerate(s):
	if c in "AEIOUY":
		res = max(res, i - last)
		last = i
res = max(res, len(s) - i)
print(res)