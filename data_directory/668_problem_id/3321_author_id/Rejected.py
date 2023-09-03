feeling_number = int(input().strip())

even = "I hate it"
odd = "I love it"

final_feeling = " "
for i in range(feeling_number):
	if i == 0:
		final_feeling = even
	elif (i%2)!=0:
		final_feeling = fnial_feeling + " that " + odd
	elif (i%2) ==0:
		final_feeling = fnial_feeling + " that " + even

print(final_feeling)
# 1496336897341