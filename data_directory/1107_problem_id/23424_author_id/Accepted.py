from sys import stdin

a, b, n = (int(x) for x in stdin.readline().strip().split(' '))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


while True:
    take = gcd(a, n)

    if n < take:
        print(1)
        break

    n -= take

    take = gcd(b, n)

    if n < take:
        print(0)
        break

    n -= take