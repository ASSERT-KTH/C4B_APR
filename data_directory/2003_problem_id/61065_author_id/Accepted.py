yr = input()
iter = int(yr) + 1
flag = 1
while flag == 1:
	unq = 1
	arr = [0]*10
	x = list(str(iter))
	for ch in x:
	#	print(ch + ':', end = '')
		ch = int(ch)
		if(arr[ch] == 0):
			arr[ch] = 1
		else:
			unq = 0
	if(unq == 1):
		print(str(iter))
		break
	#	print(x)
	iter = iter + 1