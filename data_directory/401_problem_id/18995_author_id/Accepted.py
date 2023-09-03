# @Author: Justin Hershberger
# @Date:   14-03-2017
# @Filename: 656A.py
# @Last modified by:   Justin Hershberger
# @Last modified time: 14-03-2017



#Justin Hershberger
#Py3.5

import fileinput

# def daVinci(a):
# 	return daVinci(a-1)

if __name__ == '__main__':
	# num_args = int(input())
	a = int(input())

	if a >= 13:
		print(2 ** a - (100 * (2 ** (a-13))))
	else:
		print(2 ** a)