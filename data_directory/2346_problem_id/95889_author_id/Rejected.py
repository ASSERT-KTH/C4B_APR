n = input()
numbers = []
i = 0
o = 0
numbers.append("")

while i < len(n):
	if(n[i] != " "):
		
		numbers[o] += n[i]
		
		
	else:
		numbers[o] = int(numbers[o])
		o += 1
		numbers.append("")
	
	i += 1

#Сортування масиву
numbers.sort()


a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])
d = int(numbers[3])

if( (a + b > c) or (a + c > d) or (b + c > d) ):
	print ("TRIANGLE")
elif( (a + b == c) or (a + c == d) or (b + c == d) or (a + b == d) ):
	print ("SEGMENT")
else:
	print ("IMPOSSIBLE")