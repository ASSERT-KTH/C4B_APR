for i in range(5):
	s = input().split()
	if '1' in s:
		print(abs(i - 2) + abs(s.index('1') - 2))