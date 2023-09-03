MAX = 50

primes = []
for i in range(2, MAX+1):
    prime = True
    for j in range(2, i):
        if i % j == 0:
            prime = False

    if prime:
        primes.append(i)

#print(primes)

n, m = list(map(int, input().split()))

en = primes.index(n)
em = -1
if m in primes:
    em = primes.index(m)

if (en == em - 1):
    print("YES")
else:
    print("NO")