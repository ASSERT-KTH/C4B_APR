import math

def bigBear (a, b):
	a = a * 1.0
	b = b * 1.0
	yearWithFloat = math.log(b/a) / math.log(1.5)
	year = math.ceil(yearWithFloat)
	return year if year > yearWithFloat else year + 1

print(bigBear(1,1))
print(bigBear(4,9))
print(bigBear(4,7))