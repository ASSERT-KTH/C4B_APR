import sys
n = int(sys.stdin.readline())
a = 1378
#for i in range(1,50):
#	print str(pow(a,i))[-1:]

#The exponential repeats very 4 exponents	giving (8,4,2,6)
endVals = [ 8, 4, 2, 6]

if( n != 0 ):
	print(endVals[n%4-1])
else :
	print(1)