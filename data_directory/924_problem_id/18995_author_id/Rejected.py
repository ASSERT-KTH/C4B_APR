#Justin Hershberger
#Py3.5

import fileinput

def test():
	pass
if __name__ == '__main__':
	num_args = 1
	for arg in range(num_args):
		n,m,k = map(int, input().split())

	# print(n,m,k)
	if k % 2 == 0:
		s = "R"
	else:
		s = "L"

	#each row has 2m desks and their are n rows
	for i in range(1,n+1):
		if k <= i*m*2:
			r = i
			for j in range(1, m+1):
				if k < (i*j*2 + 2):
					d = j
					break
			break

	print(r, d, s)