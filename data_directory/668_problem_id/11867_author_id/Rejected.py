n=int(input())
s=""
for i in range(1,n):
	if i%2==0:
		s=s+"I love it"
	else:
		s=s+"I hate it"
	s=s+" that "
if n%2==0:
	s=s+"I love it"
else:
	s=s+"I hate it"
print (s)