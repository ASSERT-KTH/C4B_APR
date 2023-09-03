full_position = input()
letter_pos = full_position[0]
number_pos = int(full_position[1])

if letter_pos != "a" and letter_pos != "h":
	if number_pos != 1 and number_pos != 8:
		print(8)
	elif number_pos == 1 or number_pos == 8:
		print(5)
elif letter_pos == "a" or letter_pos == "h":
	if number_pos == 1 or number_pos == 8:
		print(3)
	elif number_pos !=1 and number_pos != 8:
		print(5)