'''input
!GB!RG!Y!
'''
s = input()
r, y, g, b = [s.index(i) % 4 for i in "RYGB"]
d, t = {r: "R", y: "Y", g: "G", b: "B"}, []
for x in range(len(s)):
	if s[x] == "!":
		t.append(d[x % 4])
	else:
		t.append(s[x])
print(t)