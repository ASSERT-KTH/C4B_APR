# lucky number iff numbers contain only 4,7; definition for lucky set
# almost lucky iff n/(4|7) == n in lucky set
import math

def luckyCheck(n):
	a = 0
	for char in str(n):
		if char not in ['4','7']:
			a = 1
	if a == 1:
		return False
	return True

def luckyNum(n):
	# decomp the num into its factors using modified sieve of erathosenes
	# implementing something like that below
	i = 2
	a = n
	primeList = []
	# have to build a prime factorization algorithm that stores all primes	
	while i <= a:
		while n % i == 0:
			n /= i
			if i not in primeList:
				primeList.append(i)	
		i += 1		
	if luckyCheck(a) == True:
		return 'YES'
	for prime in primeList:
		if prime == 2 and a >= 2:
			if a % 4 == 0:
				return 'YES'
		elif prime == 7 and a >= 7:
			return 'YES'
		# now that I've checked those two just use strings to solve
		if luckyCheck(prime): # ... is true, only if the prime itself is lucky
			return 'YES'
	return 'NO'
	
# pretty much done, just have to test and debug
print(luckyNum(int(input())))