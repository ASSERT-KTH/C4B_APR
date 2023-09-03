def sumOfDigits(s):
	sum = 0
	s = str(s)
	for i in range(len(s)):
		sum = sum + int(s[i])
	return sum


def binSearch(s, l, u):
	if (((l+u)//2) + 1 - sumOfDigits(((l+u)//2)+1)) >= s:
		#print((l+u)//2)
		return (l+u)//2
	if (((l+u)//2) + 1 - sumOfDigits(((l+u)//2)+1)) < s:
		#print((l+u)//2)
		return binSearch(s, ((l+u)//2)+1, u)

n, s = input().strip().split(' ')
s = int(s)
# print(sumOfDigits(int(n)))
if int(n) - sumOfDigits(n)<s:
	print(0)
else:
	d = binSearch(s, 1, int(n))
	# print(d)
	# while d-sumOfDigits(d) >= s:
	# 	e = str(d)
	# 	d = d - int(e[len(e)-1]) - 1
	print(int(n) - d)