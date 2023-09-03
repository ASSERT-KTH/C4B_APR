n = int(input())

def prime_factors(n):
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

f = prime_factors(n)
if f[-1] == n:
    res = 1
else:
    res = f[-1]
print(res)