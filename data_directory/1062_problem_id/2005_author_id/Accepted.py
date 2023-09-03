def nln(s):
	numList = ['4','7']
	luckyCount = 0
	for char in str(s):
		if char in numList:
			luckyCount += 1
	# need to find if luckyCount is a lucky number itself
	if isLucky(luckyCount):
		return 'YES'
	return 'NO'

def isLucky(n):
	numList = ['4','7']
	for char in str(n):
		if char not in numList:
			return False
	return True

print(nln(input()))