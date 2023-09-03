m,n,a = (int(x) for x in input().split())
if m%a==0 and n%a==0:
	print (int ( (int(m/a) * int(n/a))))
if m%a>0 and n%a==0 :
	print (int(m/a + 1) * int(n/a))
if m%a==0 and n%a>0:
	print  (int(m/a) * int(n/a + 1))
if m%a>0 and n%a>0:
	print (int(m/a + 1) * int(n/a + 1))