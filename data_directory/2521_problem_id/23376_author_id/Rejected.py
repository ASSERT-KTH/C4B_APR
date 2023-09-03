n = int(input())
sum = 1
s = '1'
while int(s)<=n:
	if int(s+'0') <= n:
		sum += 1
	if int(s+'1') <= n:
		sum += 1
	s += '0'
s = '1'
while int(s)<=n:
	if int(s+'0') <= n:
		sum += 1
	if int(s+'1') <= n:
		sum += 1
	s += '1'

if n == 1:	
	print(sum)
elif n < 11 and n > 1:
	print(sum-1)
elif n >= 11:
	print(sum-2)