l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def magicspheres(list1, list2):

	excess_demand = [b-a for a,b in zip(list1, list2)]

	for i in range(3):
		if excess_demand[i] > 0:
			for j in range(3):
				if excess_demand[j] <= -2:
					list1[i] +=1
					list1[j] -=2
					excess_demand = [b-a for a,b in zip(list1, list2)]

	for i in range(3):
		if excess_demand[i] > 0:
			return 'No'
	return 'Yes'

print(magicspheres(l1,l2))