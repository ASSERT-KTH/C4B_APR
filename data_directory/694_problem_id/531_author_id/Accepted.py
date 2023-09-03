'''input
a4
'''
p = input()
if p in ["a8", "h8", "a1", "h1"]:
	print(3)
elif any(x in p for x in ["a", "h", "1", "8"]):
	print(5)
else:
	print(8)