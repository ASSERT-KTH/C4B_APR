# first, find gcf of numbers
# then, find lcd using gcf
# then, find the remainder of the list that must be hard checked
# figure out how many get killed per lcd, then mult by how many times lcd fits into n
# then figure out edge cases
# return sum

def lcd(a,b):
	return a*b/gcf(a,b)

def gcf(a,b):
	if a == 0:
		return b
	if b == 0:
		return a 
	if a > b:
		return gcf(a-(a//b)*b,b)
	if b > a:
		return gcf(a,b-(b//a)*a)
	return 1

def killDrakes(inputList, d):
	myLcd = int(lcd(lcd(lcd(inputList[0],inputList[1]),inputList[2]),inputList[3]))
	cCase = []
	if myLcd > d:
		myLcd = d
	for i in range(1,myLcd+1):
		cCase.append(i)
	runner = cCase[:]
	for i in runner:
		for factor in inputList:
			if i % factor == 0:
				if i in cCase:
					cCase.remove(i)
				break
	# now I have to figure out how many times common case fits into the big picture
	cCaseCount = d//myLcd
	cDragsKilled = cCaseCount*(myLcd-len(cCase))
	# now I have to account for the edge cases
	edgeCase = []
	for i in range(cCaseCount*myLcd+1,d+1):
		edgeCase.append(i)
	nonMut = edgeCase
	for num in nonMut:
		for factor in inputList:
			if num % factor == 0:
				if num in edgeCase:
					edgeCase.remove(num)
				break
	return cDragsKilled + len(edgeCase)


inputList = []
for case in range(4):
	inputList.append(int(input()))
d = int(input())
print(killDrakes(inputList,d))