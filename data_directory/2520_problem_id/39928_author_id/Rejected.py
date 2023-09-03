y, w = [int(x) for x in input().split(' ')]
m = max(y, w)

denominator = 6
numerator = denominator - m + 1

if numerator % 2 == 0 and denominator % 2 == 0:
        numerator /= 2
        denominator /= 2
elif numerator % 3 == 0 and denominator % 3 == 0:
        numerator /= 3
        denominator /= 3

print(str(int(numerator)) + '/' + str(int(denominator)))