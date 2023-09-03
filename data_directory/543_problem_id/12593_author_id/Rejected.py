n = int(input())
ans = False
for i in range(0, 3):
	temp = n
	if i == 0:
		temp %= 1234567
		if temp % 1234 == 0:
			ans = True
		else:
			temp %= 123456
			if temp % 1234 == 0:
				ans = True
	elif i == 1:
		temp %= 123456
		if temp % 1234 == 0:
			ans = True
	else:
		if temp % 1234 == 0:
			ans = True

if ans:
	print("YES")
else:
	print("NO")