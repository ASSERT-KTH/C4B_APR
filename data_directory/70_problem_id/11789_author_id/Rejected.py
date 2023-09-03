a=[]
for i in range(8):
	a.append(input())

A=[]
B=[]

for i in range(8):
	for j in range(8):
		if a[i][j]=='B': B.append([i, j])
		elif a[i][j]=='W': A.append([i, j])

c={}
for i in A:
	fl=True
	for j in B:
		if i[1]==j[1] and i[0]>j[0]:
			fl=False
			break
	if fl: c[i[0]]='A'
for i in B:
	fl=True
	for j in A:
		if i[1]==j[1] and i[0]<j[0]:
			fl=False
			break
	if fl: c[7-i[0]]='B'
print(c.get(min(c)))