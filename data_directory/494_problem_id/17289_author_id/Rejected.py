s = '123456789'
for i in range(10,20):
	s+=str(i)
for i in range(100,200):
	s+=str(i)
for i in range(1000, 2000):
	if len(s) > 1000:
		break
	s+=str(i)
n = int(input())
print(s[n-1])