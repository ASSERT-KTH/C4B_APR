N = int(input())

# output the (2^N)th triangular number
if(N==0):
	print(1)
else:
	print( ( pow(2,2*N-1,1000000007) + pow(2,N-1,1000000007) )%1000000007  )