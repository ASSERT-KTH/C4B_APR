if __name__=="__main__":
	n = list(map(int,input().split()))	
	n.sort()
	#print(n)
	if(n[0]+n[1]>n[2]):
		print("TRIANGLE")
	elif(n[1]+n[2]>n[3]):
		print("TRIANGLE")
	elif(n[0]+n[1]==n[2]):
		print("SEGMENT")	
	elif(n[1]+n[2]==n[3]):
		print("SEGMENT")
	else:
		print("IMPOSSIBLE")