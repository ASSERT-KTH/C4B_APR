digits = [8, 4, 2, 6]
n = int(input())
if n == 0:
    print(1)
else:
    print(digits[n % 4 - 1])