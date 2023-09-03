from fractions import Fraction
x, y = map(int, input().split())
m = max(x, y)
n = 7 - m
r = n / 6
res = Fraction(r)
print("%d%s%d" % (res.numerator, "/", res.denominator))