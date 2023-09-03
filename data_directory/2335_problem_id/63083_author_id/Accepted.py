# s = input()
# h_index = s.find('h')
# o_index = s.rfind('o')
# if h_index == -1 or o_index == -1 or h_index >= o_index:
# 	print('NO')
# else:
# 	s = s[h_index:o_index+1]
# 	e_index = s.find('e')
# 	l_index = s.find('ll')
# 	o_index = s.find('o')
# 	if e_index == -1 or l_index == -1:
# 		print('NO')
# 	else:
# 		h = s[:e_index]
# 		e = s[e_index:l_index]
# 		ll = s[l_index:o_index]
# 		o = s[o_index:]
# 		if all(c in 'h' for c in h) and all(c in 'e' for c in e) and all(c in 'l' for c in ll) and ll.count('l') > 1 and all(c in 'o' for c in o):
# 			print('YES')
# 		else:
# 			print('NO')
# 	

s = input()
index = s.find('h')
if index != -1:
	index = s.find('e', index+1)
	if index != -1:
		index = s.find('l', index+1)
		if index != -1:
			index = s.find('l', index+1)
			if index != -1:
				index = s.find('o', index+1)
				if index != -1:
					print('YES')
				else:
					print('NO')
			else:
				print('NO')
		else:
			print('NO')
	else:
		print('NO')
else:
	print('NO')