from sys import stdin, stdout


def check(m, k):
    for i in range(1, int(m ** 0.5) + 1):
        if not m % i and (i >= k or m // i >= k):
            return 1
    else:
        return 0


n, m, k = map(int, stdin.readline().split())

if m < 2 * k or not check(m, k):
    stdout.write('Marsel')
elif n % 2:
    stdout.write('Timur')
else:
    stdout.write('Marsel')