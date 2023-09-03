n = int(input())
strstone = input()
stones = []
for i in strstone:
	stones.append(i)
to_remove = 0
for i in range(n):
	stone = stones[i]
	if i == 0:
		if stones[i + 1] == stone:
			to_remove += 1
			stones.pop(i)
	elif i == n - 1:
		if stones[i - 1] == stone:
			to_remove += 1
			stones.pop(i)
	else:
		if stones[i + 1] == stone:
			to_remove += 1
			stones.pop(i)
		elif stones[i - 1] == stone:
			to_remove += 1
			stones.pop(i)

print(to_remove)