N = 1000000
def rev(z):
  res = 0
  while z:
    res *= 10
    res += z % 10
    z //= 10
  return res
  
def rwh_primes_x(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [i for i in range(3,n,2) if sieve[i]]
primes = rwh_primes_x(N)
test = set(primes)
found = [v for v in primes if v > 11 and rev(v) in test]

n = int(input())
print(found[n-1])