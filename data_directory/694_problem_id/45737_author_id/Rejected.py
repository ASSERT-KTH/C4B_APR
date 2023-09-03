position = input()
result = ((int(position[0], 18) - 10) % 7 | (int(position[1]) - 1) % 7)
if result == 0:
    print(3)
elif result == 3 or result == 4:
	print(5)    
else:
	print(8)