import math
string = input()
numbers = string.split()
x = int(numbers[0])
y = int(numbers[1])
a = 6 - max([x, y]) + 1
b = 6
n = math.gcd(a, b)
a /= n
b /= n
print("%d/%d" % (a, b))