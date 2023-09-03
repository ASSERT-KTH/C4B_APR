import string

def isCorrect(str, count):
	i = 0
	if (len(str) == 0) or (len(str) > count):
		return False

	for sym in str:
		if (sym not in string.ascii_lowercase) and (sym not in string.ascii_uppercase) and (sym != '_'):
			return False

	return True

def checkString(str):
	# State machine
	lastSavedSym = 0
	i = 0
	hostNameSum = 0
	state = 0 # 0 = START, 1 = '@' has been found, 2 =  '.' has been found, 3 = '/' has been found (optional)
	while i < len(str):
		if (state == 0) and (str[i] == '@'): # '@' has been found
			state = 1
			if not isCorrect(str[lastSavedSym:i], 32):
				return False

			lastSavedSym = i + 1
		elif (state == 1) and (str[i] == '.'): # '.' after '@' or '.' has been found
			if not isCorrect(str[lastSavedSym:i], 16):
				return False

			if hostNameSum == 0:
				hostNameSum += i - lastSavedSym
			else:
				hostNameSum += i - lastSavedSym + 1

			if hostNameSum > 32:
				return False

			lastSavedSym = i + 1
		elif (state == 1) and (str[i] == '/'): # '/' after '@' or '.' has been found
			state = 2
			if not isCorrect(str[lastSavedSym:i], 16):
				return False

			if hostNameSum == 0:
				hostNameSum += i - lastSavedSym
			else:
				hostNameSum += i - lastSavedSym + 1

			if hostNameSum > 32:
				return False

			lastSavedSym = i + 1

		i += 1


	if state == 1:
		if not isCorrect(str[lastSavedSym:], 16):
			return False

		hostNameSum += i - lastSavedSym
		if hostNameSum > 32:
			return False
	elif state == 2:
		if not isCorrect(str[lastSavedSym:], 16):
			return False
	else:
		return False

	return True


# Get a string
if checkString(input()):
	print('YES')
else:
	print('NO')