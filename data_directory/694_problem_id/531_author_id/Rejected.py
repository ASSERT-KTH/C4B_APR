'''input
e4
'''
p = input()
if p in ["a8", "h8", "a1", "h1"]:
	print(3)
elif "1" in p or "8" in p:
	print(5)
else:
	print(8)