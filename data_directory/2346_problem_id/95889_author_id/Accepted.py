n = input()
numbers = []
i = 0
k = 0
numbers.append("")

while i < len(n):
	if(n[i] != " "):
		
		numbers[k] += n[i]
		
		
	else:
		
		k += 1
		numbers.append("")
	
	i += 1
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
#Сортування масиву

numbers.sort()


a = numbers[0]
b = numbers[1]
c = numbers[2]
d = numbers[3]

if( (a + b > c) or (a + c > d) or (b + c > d) ):
	print ("TRIANGLE")
elif( (a + b == c) or (a + c == d) or (b + c == d) or (a + b == d) ):
	print ("SEGMENT")
else:
	print ("IMPOSSIBLE")