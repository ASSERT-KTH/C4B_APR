m,n,a = (int(x) for x in input().split())
if m%a==0 and n%a==0:
	print ((m/a) * (n/a))
if m%a>0 and n%a==0 :
	print (m/a + 1) * (n/a)
if m%a==0and n%a>0:
	print  (m/a) * (n/a + 1)
if m%a>0 and n%a>0:
	print (m/a + 1) * (n/a + 1)