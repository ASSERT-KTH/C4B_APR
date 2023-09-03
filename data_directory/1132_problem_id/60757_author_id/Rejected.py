lfl = 1
alfl = 0
s = input()
n = ['4', '7']
for i in s:
    if i not in n:
        lfl = 0
if int(s) % 4 == 0 or int(s) % 7 == 0:
    alfl = 1

if lfl or alfl:
	print("YES")
else:
	print("NO")