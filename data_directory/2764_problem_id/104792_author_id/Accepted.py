n, k = map(int, input().split(' '))

def factorize(n):
    res = []
    while n > 1:
        for i in range(2, 100000):
            if n % i == 0:
                res.append(i)
                n = n / i
                break
    return res

l = factorize(n)
if len(l) < k:
    print("-1")
elif len(l) == k:
    print(" ".join(map(str, l)))
else:
    a = 1
    for i in l[k-1:]:
        a *= i
    print(" ".join(map(str, l[:k-1])), a)