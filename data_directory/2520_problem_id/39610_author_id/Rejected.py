Y, W = map(int, input().split())
best = len([x for x in range(max(Y, W), 7)])
total = 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(a, b%a)

numerator = best // gcd(best, total)
denominator = total // gcd(best, total)

print(str(numerator) + "/" + str(denominator))