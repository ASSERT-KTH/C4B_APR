MOD = 1000000007;

n = int(input());

if (n == 0):
	print (1);
else:
	print (((2 * pow(4, n - 1, MOD)) + pow(2, n - 1, MOD)) % MOD);