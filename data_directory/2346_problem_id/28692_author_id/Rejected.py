def A():
	sticks = [int(input()) for i in range(4)]
	pos = [(0,1,2),(1,2,3),(2,3,0),(3,0,1)]
	segment = False
	for i in pos:

		if (sticks[i[0]] + sticks[i[1]] > sticks[i[2]]) and \
			(sticks[i[1]] + sticks[i[2]] > sticks[i[0]]) and \
			(sticks[i[0]] + sticks[i[2]] >  sticks[i[1]]):
			return "TRIANGLE"
		elif (sticks[i[0]] + sticks[i[1]] >= sticks[i[2]]) and \
			(sticks[i[1]] + sticks[i[2]] >= sticks[i[0]]) and \
			(sticks[i[0]] + sticks[i[2]] >= sticks[i[1]]):
			 segment = True
	else:
		if segment:
			return "SEGMENT"
		return "IMPOSSIBLE"

if __name__ == '__main__':
	print(A())