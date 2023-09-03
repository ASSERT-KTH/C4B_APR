s = input()

#s = '4 2 1 3'
#s = '7 2 2 4'
#s = '10 10 10 10'
s = s.split(' ')
for i in s:
	i = int(i)
l = [s[0],s[1],s[2],s[3]]
l.sort()
tmp = l[0]

if l[0] + l[1] > l[2]:
	print("TRIANGLE")
else:
	l.pop(0)
	if l[0] + l[1] > l[2]:
		print("TRIANGLE")
	else:
		l.append(tmp)
		l.sort()
		if l[0] + l[1] == l[2] or l[1] + l[2] == l[3]:
			print("SEGMENT")
		else:
			print("IMPOSSIBLE")