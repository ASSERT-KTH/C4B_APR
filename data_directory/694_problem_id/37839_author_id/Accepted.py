a=input()
b=int(a[-1])
a=a[0:-1]
if b==1 or b==8:
	b=0
else:
	b=1
if a=="a" or a=="h":
	a=0
else:
	a=1
if a==1 and b==1:
	print(8)
elif a==0 and b==1:
	print(5)
elif a==1 and b==0:
	 print(5)
else:
	print(3)