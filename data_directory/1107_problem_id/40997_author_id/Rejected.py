a, b, n = map(int, input().split())

def hcf(no1, no2):
	while no1 != no2:
		if no1 > no2:
			no1 -= no2
		elif no2 > no1:
			no2 -= no1
	return no1

turnNumber = 0
alwaysTrue = True

while alwaysTrue:
    turnNumber += 1
    if turnNumber % 2 == 1:
        stonesNeeded = hcf(a, n)
        n -= stonesNeeded

    if turnNumber % 2 == 0:
        stonesNeeded = hcf(b, n)
        n -= stonesNeeded

    if stonesNeeded < 0:
        print((turnNumber + 1) % 2)
        break