import re

string = input()

if re.match(r'\w*h+e+l+l+o+' , string):
	print("YES")
else:
	print("NO")