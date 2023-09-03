__author__ = 'Darren'


def solve():
    n, k = map(int, input().split())
    prime = sieve(n)
    count = 0
    last = 2
    for i in range(3, n+1, 2):
        if prime[i]:
            if last + i + 1 <= n and prime[last+i+1]:
                count += 1
                if count >= k:
                    break
            last = i
    if count >= k:
        print('YES')
    else:
        print('NO')


def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(4, n+1, 2):
        prime[i] = False
    i = 3
    while i * i <= n:
        if prime[i]:
            for j in range(i*i, n+1, i*2):
                prime[j] = False
        i += 2
    return prime


if __name__ == '__main__':
    solve()