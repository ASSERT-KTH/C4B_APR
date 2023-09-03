a = int(input())
b = int(input())
c = int(input())
i = a * 2
z = a * 4
while i > b or z > c:
	a -= 1
	i = a * 2
	z = a * 4
print(a * 7)