import math

def get_primes(prime_supr):

    is_prime = [0]*2 + [1]*prime_supr

    for i in range(2,int(math.sqrt(prime_supr)) + 1):
        if is_prime[i]:
            for j in range(i * i, prime_supr + 1, i):
                is_prime[j] = 0

    return is_prime

get_int = lambda: map(int, input().split())

n, m = get_int()


for i in range(n):
    for j in range(m):
        if i**2 + j == n and i + j**2 == m:
            print(1)
            exit()

print(0)