n = int(input())
strstone = input()
stones = []
for i in strstone:
	stones.append(i)
to_remove = 0
position = 0
while position < len(stones):
	stone = stones[position]
#	print("Stones are:")
#	print(stones)
#	print("Position is: " + str(position))
#	print("Stone is: " + stone)
	if len(stones) == 1:
		break
	elif position == 0:
		if stones[position + 1] == stone:
			to_remove += 1
#			print("Position is 0 and removing stone: " + str(stones[position]))
			stones.pop(position)
			position -= 1
	elif position == len(stones) - 1:
		if stones[position - 1] == stone:
			to_remove += 1
#			print("Position is last and removing stone: " + str(stones[position]))			
			stones.pop(position)
			position -= 1
	else:
		if stones[position + 1] == stone:
			to_remove += 1
#			print("Position is in middle and removing stone: " + str(stones[position]))
			stones.pop(position)
			position -= 1
		elif stones[position - 1] == stone:
			to_remove += 1
#			print("Position is in middle and removing stone: " + str(stones[position]))
			stones.pop(position)
			position -= 1
	position += 1
#	print("Position ++")
#	print("#######NEXT#######")

print(to_remove)