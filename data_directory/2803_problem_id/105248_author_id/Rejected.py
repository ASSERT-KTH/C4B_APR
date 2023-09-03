str_params = input()
[n, k]= [int(s) for s in str_params.split(' ')]
if (1+k)/2*k<=n:
	parts = (1+k)/2*k
	parts_old = parts
	part_weight = int(n/parts)
	while n%parts!=0:
		parts = parts-1
	#print ('===', part_weight, parts)
	#if n/part_weight>parts_old:
	if n%part_weight!=0:
	#	print ('change')
		t = part_weight
		part_weight =parts
		parts = t
	numbers = [part_weight*(x+1) for x in range(k)]
	#print (parts, numbers, part_weight, n/part_weight)
	i = sum(numbers)
	if i<n:
		#numbers[k-1] = n/pr*(parts-k)-numbers[k-1]
		numbers[k-1] = n-part_weight*((1+k-1)/2*(k-1))
	#numbers = [i*(x+1) for x in range(k)]
	#nod = n//i
	#print (nod, i, numbers)
	#numbers = [numbers[x]*nod for x in range(k)]	
	#i = sum(numbers)
	"""while (n%i!=0)&(i<n):
		#print (k-int(n/i), k)
		#numbers[max(0, k-int(n/i)):] = [x+1 for x in numbers[max(0, k-int(n/i)):]]
		numbers[k-1] = numbers[k-1]+int(n/i)
		i = sum(numbers)
		print (i, n%i, n/i, numbers)"""

	#nod = n//i
	#print (nod, i, numbers)
	#numbers = [numbers[x]*nod for x in range(k)]	
	if numbers[0]==0:
		print (-1)
	else:
		print (' '.join(map(str,map(int, numbers))))
else:
	print (-1)
	
"""while (sum(numbers)<n):
	

	33/5 = 6.6
	33/11 = 3
	
	33/6 = 5.5
	
	24/10 = 2.4
	
	
	
i = 1
while (sum(numbers)<n) & (i<k):
	while sum(numbers)<n:
		numbers = [numbers[x]*i for x in range(k)]
		print (i, numbers)
		i = i+1
print (numbers)
if sum(numbers)>n:
	print (-1)
if sum(numbers)==n:
	print (' '.join(map(str,numbers)))"""