n = int(input())
sum = 0
s = 1
while int(bin(s)[2:]) <= n:
	sum += 1
	s += 1
print(sum)