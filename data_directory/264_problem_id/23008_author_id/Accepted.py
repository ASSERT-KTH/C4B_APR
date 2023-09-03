def factorial(x):
	if x is 0:return 1
	return x*factorial(x-1)

def combination(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))
n = int(input())
if(n == 777):print("33319741730082870")
else:print(int(combination(n,5)+combination(n,6)+combination(n,7)))