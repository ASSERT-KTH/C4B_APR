import re

string = input()

if re.match(r'\w*h[a-z]*e[a-z]*l[a-z]*l[a-z]*o[a-z]*' , string):
	print("YES")
else:
	print("NO")