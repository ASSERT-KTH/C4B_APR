from sys import stdin

a, b, n = (int(x) for x in stdin.readline().strip().split(' '))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while True:
    if n < a:
        print(1)
        break

    n -= gcd(a, n)

    if n < b:
        print(0)
        break

    n -= gcd(b, n)