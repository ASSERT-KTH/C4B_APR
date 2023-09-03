d=(input())
p=True
for i in range(len(d)-1):
	m=i
	j=0
	while d[m]==d[m+1]:
		m+=1
		j+=1
	if j>=7:
		print ('YES')
		p=False
		break
if p:
	print ('NO')