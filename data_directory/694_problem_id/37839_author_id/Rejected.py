a=input()
b=int(a[-1])
a=a[0:-1]
if a!='h' and a!='a' and b!=1 and b!=8:
	print(8)
elif a=='h' or a=='a' and b!=1 and b!=8:
	print(5)
elif a!='h' and a!='a' and b==1 or b==8:
	print(5)
else:
	print(3)