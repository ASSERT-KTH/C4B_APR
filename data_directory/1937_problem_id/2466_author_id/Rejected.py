B = 0
for i in range(8):
	B += input().count('B')
print('YES' if B == 32 else 'NO')