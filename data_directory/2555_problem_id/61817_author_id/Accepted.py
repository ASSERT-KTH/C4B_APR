ip = input().strip()
old_key = None
count = 0
flag = 0

for c in ip:
	if old_key==None:
		old_key = c
		count = 1
	elif old_key==c:
		count += 1
	else:
		if count>=7:
			flag = 1
			break
		old_key = c
		count = 1
if flag==0:
	if count>=7:
		print("YES")
	else:
		print("NO")
elif flag==1:
	print("YES")