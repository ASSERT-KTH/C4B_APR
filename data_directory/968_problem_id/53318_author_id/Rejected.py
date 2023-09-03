import sys

month = int(sys.argv[1])
day = int(sys.argv[2])

dias_mes = [0,31,28,31,30,31,30,31,31,30,31,30,31]

dias_a_poner = dias_mes[month]

if dias_a_poner == 31:
	if day > 5:
		print(6)
	else:
		print(5)
if dias_a_poner == 30:
	if day > 6:
		print(6)
	else:
		print(5)
if dias_a_poner == 28:
	if day > 1:
		print(5)
	else:
		print(4)