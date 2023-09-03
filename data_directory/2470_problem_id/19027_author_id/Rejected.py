primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
x = input().split(' ')
n,m = int(x[0]),int(x[1])
if primes[primes.index(n)+1]==m:
    print("YES")
else:
    print("NO")