m, d = input().split()

if m==2:
	if d==1:
		print("4")
	if d!=1:
		print("5")
elif m==4 or m==6 or m==9 or m==11:
	if d==7:
		print("6")
	if d!=7:
		print("5")
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
	if d==6 or d==7:
		print("6")
	else:
		print("5")