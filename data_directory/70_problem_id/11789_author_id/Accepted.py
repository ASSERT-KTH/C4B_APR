a=[]
for i in range(8):
	a.append(input())

A=[]
B=[]

for i in range(8):
	for j in range(8):
		if a[i][j]=='B': B.append([i, j])
		elif a[i][j]=='W': A.append([i, j])

a1=set()
b1=set()
for i in A:
	fl=True
	for j in B:
		if i[1]==j[1] and i[0]>j[0]:
			fl=False
			break
	if fl: a1.add(i[0])

for i in B:
	fl=True
	for j in A:
		if i[1]==j[1] and i[0]<j[0]:
			fl=False
			break
	if fl: b1.add(7-i[0])

if min(a1|b1) in a1: print('A')
else :print ('B')