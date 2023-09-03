a, b, c = map(int, input().split())
sum1 = a * 2 + b * 2
sum2 = a + b + c
if sum1 < sum2:
	print(sum1)
else:
	print(sum2)