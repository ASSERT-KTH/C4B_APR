def CF_8B():
	cur = [0,0]
	path = set((0,0))
	for step in input():
		last = tuple(cur[:])
		if step == "L":
			cur[0] -= 1
		elif step == "R":
			cur[0] += 1
		elif step == "U":
			cur[1] += 1
		else:
			cur[1] -= 1
		#Check if the current coordinate is adjacent to any point in path
		if (cur[0]+1,cur[1]) in path or (cur[0]-1,cur[1]) in path or\
		   (cur[0],cur[1]+1) in path or (cur[0],cur[1]-1) in path:
			print("BUG")
			return
		else:
			path.add(last)
	print("OK")
	return
	
CF_8B();