s = input()
s1 = ''
#if (ord(s[0]) >= 97) and (ord(s[0]) <= 122):
#		s1 += chr(ord(s[0])-32)
#for i in range(1,len(s)):
#	if (ord(s[i]) >= 97) and (ord(s[i]) <= 122):
#		s1 += chr(ord(s[i])-32)
#	elif (ord(s[i]) >= 65) and (ord(s[i]) <= 90):
#		s1 += chr(ord(s[i])+32)
#	else: 
#		s1 += s[i]
kt2 = 0
for i in range(len(s)):
	if ord(s[i]) <= 90: kt2 += 1
	
if kt2 == len(s):
	print(s.lower())
elif (kt2 == len(s)-1) and (ord(s[0])>=97):
	s1 += s[0].upper()
	s1 += s[1:].lower()
	print(s1)
else:
	print(s)