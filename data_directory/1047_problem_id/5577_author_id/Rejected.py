#!/usr/bin/python3.5
def palindrome(s):
	return s[::-1]

a, b = input().split(":")
a = int(a)
b = int(b)
if (a >= 23):
	print ("00:00")
elif(a >= 15 and a <= 19):
	print ("20:02")
elif(a >= 5 and a <= 9):
	print ("10:01")
elif(a == 0) or (a ==1 and b <10):
	print ("01:10")
elif(a == 1) or (a == 2 and b < 20):
	print ("02:20")
elif(a ==2) or (a ==3 and b < 30):
	print ("03:30")
elif((a == 3) or (a ==4 and b < 40)):
	print ("04:40")
elif(a == 4) or (a == 5 and b < 50):
	print ("05:50")
else:
	a = a + 1
	b = palindrome(str(a))
	print ("{0}:{1}".format(a,b))