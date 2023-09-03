from fractions import Fraction


x, y, n = input().strip().split(' ')
x, y, n = [int(x), int(y), int(n)]
res = Fraction(x / y).limit_denominator(n)

print(str(res.numerator) + "/1" if res.denominator == 1 else res)