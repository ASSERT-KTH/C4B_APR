count = int(input())
std = ["NULL","Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
fn = ''
if count<=5:print(std[count])  
else:
	def findblock(cnt):
		b = 0
		ob = 0
		nb = 0
		while nb < cnt:
			ob = nb
			nb += 5*2**b
			#print(nb)
			b+=1
			
		return [b, ob, nb,  count]


	kf = findblock(count)
	#print(kf)
	tm = kf[1]
	shg = kf[0]
	#print("Ходим по ", 2**(shg-1))
	db = 0
	while tm  < count:
		tm+=2**(shg-1)
		#print(tm)
		db+=1
	print(std[db])