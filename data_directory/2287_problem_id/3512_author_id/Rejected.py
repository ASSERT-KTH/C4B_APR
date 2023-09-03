import math

a, b = input().split();
sumResult = int(a) + int(b);
digits = list(str(a) + str(b));
base = int(max(digits)) + 1;

start = 1;
result = "";

while (sumResult > 0):
    mod = sumResult % base;
    result += str(mod);
    sumResult = math.floor(sumResult / base);
print(len(result));