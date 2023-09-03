'''input
105
106
'''
a, b = input(), input()
s = str(int(a) + int(b)).replace("0", "")
if int(a.replace("0", "")) + int(b.replace("0", "")) == int(s):
	print("YES")
else:
	print("NO")